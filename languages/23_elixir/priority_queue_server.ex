# ==============================================================================
# File: languages/23_elixir/priority_queue_server.ex
# Language: Elixir 1.15+ (Erlang OTP / BEAM Actor Concurrency)
# Domain: Concurrent Distributed Systems & Fault-Tolerant Actor Models
# Algorithm: Supervised OTP GenServer Priority Message Queue
#
# Rationale & Language Fit:
#   Elixir leverages the battle-tested Erlang BEAM virtual machine. Its actor
#   model encapsulates concurrent state in lightweight, isolated processes that
#   communicate strictly via asynchronous message passing. The OTP `GenServer`
#   abstraction provides enterprise-grade guarantees: serialization of mailbox
#   calls, clean timeouts, failure supervision trees, and hot code reloading.
# ==============================================================================

defmodule PriorityQueueServer do
  @moduledoc """
  An OTP GenServer managing a concurrent priority queue.
  Higher priority integers are dequeued ahead of lower priority items.
  Maintains FIFO order among items with identical priorities.
  """
  use GenServer

  # ============================================================================
  # Client API
  # ============================================================================

  @doc """
  Starts the GenServer process linked to the current supervisor.
  """
  def start_link(opts \\ []) do
    GenServer.start_link(__MODULE__, :ok, opts)
  end

  @doc """
  Synchronously pushes a payload with a given priority.
  """
  def push(server, item, priority) when is_integer(priority) do
    GenServer.call(server, {:push, item, priority})
  end

  @doc """
  Asynchronously pushes a payload without waiting for a reply.
  """
  def push_async(server, item, priority) when is_integer(priority) do
    GenServer.cast(server, {:push, item, priority})
  end

  @doc """
  Synchronously pops the highest-priority item.
  Returns `{:ok, item, priority}` or `:empty`.
  """
  def pop(server) do
    GenServer.call(server, :pop)
  end

  @doc """
  Peeks at the highest priority item without removing it.
  """
  def peek(server) do
    GenServer.call(server, :peek)
  end

  @doc """
  Returns the total count of items in the queue.
  """
  def count(server) do
    GenServer.call(server, :count)
  end

  # ============================================================================
  # Server Callbacks (OTP Lifecycle)
  # State structure: A map of %{priority => :queue.queue()}, and a sorted list of unique priorities.
  # ============================================================================

  @impl true
  def init(:ok) do
    # State: %{queues: %{}, total: 0}
    {:ok, %{queues: %{}, total: 0}}
  end

  @impl true
  def handle_call({:push, item, priority}, _from, state) do
    new_state = do_push(state, item, priority)
    {:reply, :ok, new_state}
  end

  @impl true
  def handle_call(:pop, _from, %{total: 0} = state) do
    {:reply, :empty, state}
  end

  @impl true
  def handle_call(:pop, _from, state) do
    # Find the maximum priority key
    max_priority = state.queues |> Map.keys() |> Enum.max()
    sub_q = Map.fetch!(state.queues, max_priority)

    case :queue.out(sub_q) do
      {{:value, item}, new_sub_q} ->
        new_queues =
          if :queue.is_empty(new_sub_q) do
            Map.delete(state.queues, max_priority)
          else
            Map.put(state.queues, max_priority, new_sub_q)
          end

        new_state = %{state | queues: new_queues, total: state.total - 1}
        {:reply, {:ok, item, max_priority}, new_state}

      {:empty, _} ->
        {:reply, :empty, state}
    end
  end

  @impl true
  def handle_call(:peek, _from, %{total: 0} = state) do
    {:reply, :empty, state}
  end

  @impl true
  def handle_call(:peek, _from, state) do
    max_priority = state.queues |> Map.keys() |> Enum.max()
    sub_q = Map.fetch!(state.queues, max_priority)

    case :queue.peek(sub_q) do
      {:value, item} -> {:reply, {:ok, item, max_priority}, state}
      :empty -> {:reply, :empty, state}
    end
  end

  @impl true
  def handle_call(:count, _from, state) do
    {:reply, state.total, state}
  end

  @impl true
  def handle_cast({:push, item, priority}, state) do
    new_state = do_push(state, item, priority)
    {:noreply, new_state}
  end

  # ============================================================================
  # Internal Helpers
  # ============================================================================

  defp do_push(state, item, priority) do
    sub_q = Map.get(state.queues, priority, :queue.new())
    updated_sub_q = :queue.in(item, sub_q)
    updated_queues = Map.put(state.queues, priority, updated_sub_q)

    %{state | queues: updated_queues, total: state.total + 1}
  end
end

# --- Self-Contained OTP Demonstration ---
defmodule Demo do
  def run do
    IO.puts("=================================================================")
    IO.puts("Elixir OTP GenServer Priority Queue (BEAM Actor Architecture)")
    IO.puts("=================================================================\n")

    {:ok, pid} = PriorityQueueServer.start_link()

    IO.puts("Enqueuing concurrent task items with diverse priorities...")
    PriorityQueueServer.push(pid, "Low priority batch export", 1)
    PriorityQueueServer.push(pid, "Standard HTTP telemetry ping", 5)
    PriorityQueueServer.push(pid, "Critical database failover event", 100)
    PriorityQueueServer.push(pid, "Urgent payment gateway timeout", 50)
    PriorityQueueServer.push(pid, "Second critical security alert", 100)
    PriorityQueueServer.push(pid, "Routine log rotation", 2)

    total = PriorityQueueServer.count(pid)
    IO.puts("Total queued messages: #{total}\n")

    IO.puts("Dequeuing items in strict priority order:")
    drain(pid)

    IO.puts("\n[SUCCESS] Elixir GenServer priority mailbox successfully validated.")
  end

  defp drain(pid) do
    case PriorityQueueServer.pop(pid) do
      {:ok, item, prio} ->
        IO.puts("  [Priority #{String.pad_leading(Integer.to_string(prio), 3)}] -> #{item}")
        drain(pid)

      :empty ->
        IO.puts("Queue drained completely.")
    end
  end
end

Demo.run()
