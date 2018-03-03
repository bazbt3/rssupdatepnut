<img src="rssupdatepnut_logo.jpg" height="96" alt="rssupdatepnut RSS feed updates post to pnut.io."> <br>

# What is 'rssupdatepnut'?
A Python 3.5 application to post notifications to pnut.io and Twitter when an RSS feed is updated.

Application is currently tested in Pythonista iOS and my web host. Whilst it can run standalone it's more likely to be useful when run every hour (or 2, 3…) either as a pythonanywhere 'task' or a cron job at a web host.

### Prerequisites:
* a pnut.io account,
* pnut.io application token - read from a separate file to give some portability to the code:
 * `pnut_app_token.txt`
* The PNUTpy libraries: `pip install pnutpy`.
* The feedparser RSS, er… feed parser: `pip install feedparser`.
* A means of achieving Twitter auth to post, e.g. my [TwigPen module.](https://github.com/bazbt3/TwigPen)

Note: the code can be run with minor modifications to alert independently of a pnut.io account. Put simply, add stuff to make it happen. Er…

So I did, TwigPen, a post-only wrapper to post to Twitter using Twython.
