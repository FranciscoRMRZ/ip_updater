# ip_updater

There are times that the Dyn ip client doesn't work as intended, or the local 
modem doesn't update the record when is supposed to.
Because of that, my work flow can be hindered quite a bit. If it happens within
business hours it just takes a message or phone call to get the current address
and update it manually, but there are time when this is not possible.
Since people sometimes can't take my calls, or there isn't anyone around, I took
to myself to write this script to check the public IP every five minutes. If it
changed, it will send an email; if not, nothing happens.

Maybe I'll add some more features in the future to emulate Dyn up to a minimal
level.