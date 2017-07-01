# bit-notify
SMS notifier for bittrex

## Installation
```
$ pip install bit-notify
```

### Install from source
```
$ git clone  https://github.com/hthompson6/bit-notify.git
$ cd bit-notify
$ python setup.py install -e .
```

## Usage
Please note that this service relies on Twilio. To sign up for Twilio please
visit https://www.twilio.com/try-twilio.

```python
api_key = 'my_bittrex_api_key'
api_sign = 'my_bittrex_api_secret'
account_sid = 'my_twilio_account_sid'
auth_token = 'my_twilio_auth_token'
sender = '<country_code><my_twilio_phone_number>'
reciever = '<country_code><my_personal_phone_number>'

notify = Notifier(api_key, api_sign, account_sid, auth_token, sender, reciever)
notify.start()
```

### Advanced Usage
Notifications occur when the percent change over a 24hr span of time
lies outside of the given threshold. (Updates to this percentage are
checked every 30 minutes.)

The default is as follows: **-100% < %change < 100%**

To alter the threshold simply modify the class instatiaion:
```python
notify = Notifier(api_key, api_sign, account_sid, auth_token,
                  sender, reciever, lower_bound=-15, upper_bound=50)
notify.start()
```
