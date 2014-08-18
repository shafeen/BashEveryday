# all the essentials I would need when setting
# up a new ubuntu server or personal computer

$essentials = [ 'gcc', 'g++', 'vim', 'emacs', 'git', 'openssh-server', 'tmux', 'default-jre' ]

 
package { $essentials:
    ensure => 'installed'
}
