# rsync-backup.py
##Incremental Backups with rsync##
Wraps rsync to make incremental backups. Intended to be used with cron
and ssh RSA automatic login.

###Usage:
`python rsync-backup.py SRC DEST [--prefix] [OPTIONS]`

The script uses:

1. --archive, --backup, --backup-dir, --delete, --hard-links, --exclude
   and --checksum rsync's options to create the incremental backups.
2. --prefix is an optional extra option. Allows to change the name of the
   directories where the incremental modifications are saved. (Defaut
   is __bak_).
3. The rest of rsync options specified are bypassed to rsync. E.g. you can
   use --dry-run to performe a trial run with no changes.

###Examples:

`python rsync-backup.py ~/Downloads ~/backups/rs/MyDownloads`

`python rsync-backup.py user1@.example.com:/home/user/webapps/ /home/user1/backups/rs/webapps/ --log-file=/home/user1/backups/rs/webapps_rsb.log`
