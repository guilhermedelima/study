#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#Enable colors to grep and ls
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

#Load bash alias if exists
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

#Default
#PS1='[\u@\h \w]\$ '

PS1='[\u@\h \[\e[0;32m\]\w\[\e[0m\]]\$ '

# Check for git __git_ps1 function
GIT_PROMPT_FILE=/usr/share/git/git-prompt.sh
if [ -f $GIT_PROMPT_FILE ]; then
    source $GIT_PROMPT_FILE
    PS1='[\u@\h \[\e[0;32m\]\w$(__git_ps1 " \e[93m(%s)")\[\e[0m\]]\$ '
fi
