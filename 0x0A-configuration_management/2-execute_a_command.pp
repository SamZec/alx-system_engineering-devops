# 2-execute_a_command.pp
# create a manifest that kills a process named killmenow.

exec {'pkill -f killmenow':
  path => ['/usr/bin', '/usr/bin',],
}
