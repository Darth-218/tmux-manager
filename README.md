# What I want to do (for now)
- Session creation
- Session deletion
# Session creation
- Basic command:
```shell
tm new <session-name>
```
## Additional options/flags
- n/a
## Session creation steps
1. Get the current path.
2. Create the new session.
3. Switch to the new session
4. Set the specified session name
# Session deletion
- Basic command:
```shell
tm kill <session-name>
tm kill -x <session-name>
```
## Additional options/flags
- `-x`: delete all sessions except current/chosen session
