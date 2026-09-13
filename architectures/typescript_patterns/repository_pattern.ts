/**
 * Repository and Unit of Work Pattern in TypeScript.
 * Decouples domain logic from persistence mechanisms with atomic commit semantics.
 */

export interface Entity {
    id: string;
}

export interface IRepository<T extends Entity> {
    findById(id: string): Promise<T | null>;
    save(item: T): Promise<void>;
    delete(id: string): Promise<void>;
}

export class InMemoryRepository<T extends Entity> implements IRepository<T> {
    protected storage = new Map<string, T>();

    async findById(id: string): Promise<T | null> {
        return this.storage.get(id) ?? null;
    }

    async save(item: T): Promise<void> {
        this.storage.set(item.id, { ...item });
    }

    async delete(id: string): Promise<void> {
        this.storage.delete(id);
    }
}

export interface UnitOfWork {
    registerNew<T extends Entity>(repo: IRepository<T>, entity: T): void;
    registerClean<T extends Entity>(entity: T): void;
    commit(): Promise<void>;
    rollback(): void;
}

export class SimpleUnitOfWork implements UnitOfWork {
    private newEntities: { repo: IRepository<any>; entity: Entity }[] = [];

    registerNew<T extends Entity>(repo: IRepository<T>, entity: T): void {
        this.newEntities.push({ repo, entity });
    }

    registerClean<T extends Entity>(_entity: T): void {}

    async commit(): Promise<void> {
        for (const op of this.newEntities) {
            await op.repo.save(op.entity);
        }
        this.newEntities = [];
    }

    rollback(): void {
        this.newEntities = [];
    }
}

interface User extends Entity {
    name: string;
    email: string;
}

async function verify() {
    const userRepo = new InMemoryRepository<User>();
    const uow = new SimpleUnitOfWork();

    const u1: User = { id: "usr_1", name: "Igor Kan", email: "igorkan010@gmail.com" };
    uow.registerNew(userRepo, u1);

    // Prior to commit, repository has not persisted
    let found = await userRepo.findById("usr_1");
    if (found !== null) throw new Error("Entity persisted prior to commit");

    await uow.commit();
    found = await userRepo.findById("usr_1");
    if (!found || found.name !== "Igor Kan") {
        throw new Error("Commit failed to persist entity");
    }

    console.log("[TS Patterns] Repository & Unit of Work verified.");
}

verify();
