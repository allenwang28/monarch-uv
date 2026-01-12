"""A simple Monarch actor example demonstrating torchmonarch with uv."""

from monarch.actor import Actor, endpoint, this_host


class Counter(Actor):
    def __init__(self, initial_value: int):
        self.value = initial_value

    @endpoint
    def increment(self) -> None:
        self.value += 1

    @endpoint
    def get_value(self) -> int:
        return self.value


def main():
    print("Creating proc mesh...")
    procs = this_host().spawn_procs(per_host={"gpus": 1})
    print(f"Procs: {procs}")

    print("Spawning counter actor...")
    counter = procs.spawn("counter", Counter, initial_value=0)
    print(f"Counter: {counter}")

    print("Getting initial value...")
    value = counter.get_value.call().get()
    print(f"Initial value: {value}")

    print("Incrementing...")
    counter.increment.call().get()

    print("Getting new value...")
    value = counter.get_value.call().get()
    print(f"New value: {value}")

    print("Done!")


if __name__ == "__main__":
    main()
