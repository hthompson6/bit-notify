# MIT License
# 
# Copyright (c) 2017 Hunter Thompson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from threading import Thread

from bit_bind.api.bind import BittrexAPIBind
from sms.sms_client import SMSClient

class Notifier(Thread):

    def __init__(self, api_key, api_sign, account_sid, auth_token,
                 sender, reciever, lower_bound=-100, upper_bound=100):

       self.bit_api = BittrexAPIBind(api_key, api_sign)
       self.client = SMSClient(account_sid, auth_token, sender, reciever)
       self.lower_bound = lower_bound
       self.upper_bound = upper_bound
       self.KILLFLAG = 0

       super(Notifier, self).__init__()

    def _compute_percentage(self, currency_base, currency_market):
        prevDay, last = self.bit_api.get_market_summary(currency_base,
                                                        currency_market)

        return (float((last-prevDay))/float(prevDay)) * 100
       
    def push_notification(self, updates):
        msg = ""
        for update in updates:
            msg += ('{}\n').format(updates)

        self.client.message_create(msg)

    def kill_thread(self):
        self.KILLFLAG = 1

    def run(self):
        while not self.KILLFLAG:
            wallet = self.bit_api.get_balances()
            updates = []
            for currency in wallet:
                percentage = self._compute_percentage('btc',
                                                   currency.get('Currency').lower())
                if percentage < self.lower_bound:
                    msg = ('{}-{} has fallen by {}').format('btc', currency.get('Currency').lower(), percentage)
                    updates.append(msg)
                elif percentage > self.upper_bound:
                    msg = ('{}-{} has risen by {}').format('btc', currency.get('Currency').lower(), percentage)
                    updates.append(msg)
            if updates:
                self.push_notification(updates)

            time.sleep(180)
            self.KILLFLAG = 1
