# frozen_string_literal: true
# Thread-safe Token Bucket Rate Limiter with Monotonic Clock.
#
# Why Ruby for this module?
# Ruby excels in expressive, dynamic API service rate-limiting (Rack middleware, Sidekiq queues).

require monitor

class TokenBucketRateLimiter
  include MonitorMixin

  attr_reader :capacity, :refill_rate

  def initialize(capacity, refill_rate)
    super()
    @capacity = capacity.to_f
    @refill_rate = refill_rate.to_f # tokens per second
    @tokens = capacity.to_f
    @last_refill = Process.clock_gettime(Process::CLOCK_MONOTONIC)
  end

  def allow?(tokens_needed = 1.0)
    synchronize do
      refill!
      if @tokens >= tokens_needed
        @tokens -= tokens_needed
        true
      else
        false
      end
    end
  end

  private

  def refill!
    now = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    elapsed = now - @last_refill
    @last_refill = now
    @tokens = [@capacity, @tokens + (elapsed * @refill_rate)].min
  end
end

if __FILE__ == $PROGRAM_NAME
  limiter = TokenBucketRateLimiter.new(5, 2)
  puts "Ruby Rate Limiter initialized: 5 initial tokens"
  5.times { |i| puts "Request #{i+1}: #{limiter.allow?}" }
  puts "Request 6 (should fail): #{limiter.allow?}"
end
