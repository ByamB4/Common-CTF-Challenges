import angr
import claripy


BASE_ADDR = 0x400000


def rebase(addr):
    return BASE_ADDR + addr


def main():
    p = angr.Project("<FILENAME>")

    # 64 bytes argv[1]
    argv1 = claripy.BVS("argv1", 8*64)
    initial_state = p.factory.entry_state(args=["./teleport", argv1])

    sm = p.factory.simulation_manager(initial_state)

    # 0x1732 = good boy
    #  00101732 48 8d 3d ec 00 00 00     LEA                  argc,[s_Looks_good_to_me!_00101825]
    #  00101739 e8 a2 f2 ff ff           CALL                 <EXTERNAL>::puts

    # 0x1740 = nop
    #  00101740 48 8d 3d f0 00 00 00     LEA                  argc,[s_Something's_wrong..._00101837]
    #  00101747 e8 94 f2 ff ff           CALL                 <EXTERNAL>::puts

    sm.explore(find=rebase(0x1732), avoid=rebase(0x1740))

    if not len(sm.found):
        print("no solution")
        return 1

    found = sm.found[0]
    solution = found.solver.eval(argv1, cast_to=bytes)
    solution = solution[:solution.find(b'\x00')]
    return solution


if __name__ == "__main__":
    print([main()])
