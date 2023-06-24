# 1-install_a_package.pp
# install flask from pip3.

package {'flask':
  ensure   => ['2.1.0', 'installed'],
  provider => 'pip3',
}
