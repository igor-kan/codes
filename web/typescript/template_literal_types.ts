// Template literal types and inference.
export type EventName = "click" | "focus" | "blur";
export type HandlerName = `on${Capitalize<EventName>}`;

export type Route = `/api/${string}`;
export type RouteParams<R extends string> =
  R extends `${string}:${infer Param}/${infer Rest}`
    ? Param | RouteParams<`/${Rest}`>
    : R extends `${string}:${infer Param}`
      ? Param
      : never;

type Params = RouteParams<"/users/:userId/posts/:postId">;

export function makeHandler(name: EventName): HandlerName {
  return `on${name[0].toUpperCase()}${name.slice(1)}` as HandlerName;
}
