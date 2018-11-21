"""
The lambda statement in Python is simply an anonymous function, mostly use in the
function sorted function, or any specific function that allow to provide the
specific logic
"""


class Spam:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.value)


spams = [Spam(13), Spam(1), Spam(5), Spam(8)]
sorted_spams = sorted(spams, key=lambda spam: spam.value)
print(sorted_spams)
