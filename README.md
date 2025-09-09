# flaskapp


## Cmd

```bash
# new branch
git checkout -b feature-1

git checkout -b feature-2

# create worktree
git worktree add /tmp/feature-1 feature-1

git worktree add /tmp/feature-2 feature-2

# list
git worktree list


# use worktree

cd /tmp/feature-1
cd /tmp/feature-2

# remove worktree (when developement done in worktree)

git worktree remove /tmp/feature-1

```