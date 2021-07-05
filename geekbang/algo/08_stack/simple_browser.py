from linked_stack import LinkedStack


class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self._top


class Browser():
    def __init__(self):
        self.forward_stack = NewLinkedStack()
        self.back_stack = NewLinkedStack()

    def can_forward(self):
        if self.forward_stack.is_empty():
            return False
        return True

    def can_back(self):
        if self.back_stack.is_empty():
            return False
        return True

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.back_stack.push(url)

    def back(self):
        if self.back_stack.is_empty():
            return

        url = self.back_stack.pop()
        self.forward_stack.push(url)
        print("back to %s" % url)

    def forward(self):
        if self.forward_stack.is_empty():
            return

        url = self.forward_stack.pop()
        self.back_stack.push(url)
        print("back to %s" % url)


if __name__ == '__main__':

    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
