## Changelog
(most recent first)

### v0.2 2018-02-19:
* Changed from sending public messages to sending public posts. Note: application not tested with a blog post prior to this change.
* Removed unnecessary print command.

### v0.1 2018-02-16:
* Changed from examining 10 posts to just the most recent one. The intention is to run this as a cron job every hour (perhaps 2); it's unlikely I'll create a blog post more frequently.
* Added the creation of a message in my pnut.io dev channel if a new blog post exists.
* Next step: must create a new pnut.io app to create an independent token. (Currently borrowing the one from `crypto`!)

### v0.0 2018-02-15:
* First commit with basic functionality
 * Gets most recent 10 posts from feed.
 * Saves them to a file for later comparison with historic posts.
 * If the 'base' file doesn't exist, also saves the most recent 10 posts to a file for later comparison with more recent posts.
