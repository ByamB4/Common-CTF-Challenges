import angr

p = angr.Project('./filename', auto_load_libs=False)
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)

sm.explore(find=lambda s: b'CORRECT' in s.posix.dumps(1),
           avoid=lambda s: b'WRONG' in s.posix.dumps(1))

print(sm.found[0].posix.dumps(0))
