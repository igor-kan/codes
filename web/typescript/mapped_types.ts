// Mapped and conditional types.
export type Flags<T> = {
  [K in keyof T as `is${Capitalize<string & K>}`]: boolean;
};

export interface Features {
  admin: boolean;
  beta: boolean;
}

export type FeatureFlags = Flags<Features>;

export type Keys = keyof Features;

export type Unwrap<T> = T extends Promise<infer U> ? U : T;

export type UnwrappedNumber = Unwrap<Promise<number>>;

export type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};
