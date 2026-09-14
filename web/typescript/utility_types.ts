// Built-in utility types.
export interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

export type UserDraft = Omit<User, "id" | "createdAt">;
export type UserUpdate = Partial<Pick<User, "name" | "email">>;
export type UserIndex = Record<string, User>;
export type ReadonlyUser = Readonly<User>;
export type RequiredUser = Required<User>;
export type Preview = Pick<User, "id" | "name"> & { avatarUrl?: string };

export function toPreview(user: User): Preview {
  return { id: user.id, name: user.name };
}
