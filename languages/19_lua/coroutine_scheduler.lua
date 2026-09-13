-- Cooperative Multi-Tasking Green-Thread Scheduler using Lua Coroutines.
-- 
-- Why Lua for this module?
-- Lua's asymmetric first-class coroutines provide the fastest, most lightweight
-- embedded cooperative concurrency engine for gaming loops (Roblox, World of Warcraft) and NGINX (OpenResty).

local Scheduler = {}
Scheduler.__index = Scheduler

function Scheduler.new()
    return setmetatable({ tasks = {} }, Scheduler)
end

function Scheduler:spawn(fn)
    local co = coroutine.create(fn)
    table.insert(self.tasks, co)
end

function Scheduler:run()
    while #self.tasks > 0 do
        local current_tasks = self.tasks
        self.tasks = {}
        for _, co in ipairs(current_tasks) do
            if coroutine.status(co) ~= "dead" then
                local ok, err = coroutine.resume(co)
                if not ok then
                    error("Coroutine error: " .. tostring(err))
                end
                if coroutine.status(co) ~= "dead" then
                    table.insert(self.tasks, co)
                end
            end
        end
    end
end

-- Example usage
local sched = Scheduler.new()
sched:spawn(function()
    for i = 1, 3 do
        print("Task A: step " .. i)
        coroutine.yield()
    end
end)

sched:spawn(function()
    for i = 1, 3 do
        print("Task B: step " .. i)
        coroutine.yield()
    end
end)

print("Starting Lua Cooperative Scheduler:")
sched:run()
