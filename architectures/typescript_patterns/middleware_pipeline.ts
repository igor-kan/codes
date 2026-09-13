/**
 * Modern Middleware Pipeline / Onion Architecture Pattern in TypeScript.
 * Provides composable interceptor chaining with next() continuation semantics.
 */

export type Context = {
    state: Record<string, any>;
    requestId: string;
    path: string;
};

export type NextFunction = () => Promise<void>;
export type Middleware = (ctx: Context, next: NextFunction) => Promise<void>;

export class Pipeline {
    private middlewares: Middleware[] = [];

    public use(middleware: Middleware): this {
        this.middlewares.push(middleware);
        return this;
    }

    public async execute(ctx: Context): Promise<void> {
        let index = -1;

        const dispatch = async (i: number): Promise<void> => {
            if (i <= index) {
                throw new Error("next() called multiple times");
            }
            index = i;
            const fn = this.middlewares[i];
            if (!fn) return;

            await fn(ctx, () => dispatch(i + 1));
        };

        await dispatch(0);
    }
}

// Verification Test
async function runTest() {
    const pipeline = new Pipeline();
    const trace: string[] = [];

    pipeline.use(async (ctx, next) => {
        trace.push("M1_IN");
        ctx.state.auth = true;
        await next();
        trace.push("M1_OUT");
    });

    pipeline.use(async (ctx, next) => {
        trace.push("M2_IN");
        ctx.state.cached = false;
        await next();
        trace.push("M2_OUT");
    });

    const ctx: Context = { state: {}, requestId: "req-123", path: "/api/algorithms" };
    await pipeline.execute(ctx);

    const expectedTrace = ["M1_IN", "M2_IN", "M2_OUT", "M1_OUT"];
    if (JSON.stringify(trace) !== JSON.stringify(expectedTrace)) {
        throw new Error(`Trace mismatch: ${JSON.stringify(trace)}`);
    }
    if (!ctx.state.auth) {
        throw new Error("State mutation failed");
    }

    console.log("[TS Patterns] Middleware Onion Pipeline verified successfully.");
}

runTest();
