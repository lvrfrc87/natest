#!/usr/bin/env python3
import os

class tmTest():

    def __init__(self,input, want, have):
        self.input = input
        self.want = want
        self.have = have


    def read(self):
        fixture_list = list()
        open_fixture = open('./fixtures/{}'.format(self.input), 'r')

        for line in open_fixture:
            fixture_list.append(line)

        return fixture_list


    def result(self):

        want_list = list()
        have_list = list()

        read_want = open('./fixtures/{}'.format(self.want), 'r')

        for line in read_want:
            want_list.append(line)

        if type(self.have) is 'list':
            have_list = self.have
        else:
            for line in self.have:
                have_list.append(line)

        want_diff = [diff for diff in want_list if diff not in have_list]
        have_diff = [diff for diff in have_list if diff not in want_list]
        print(want_diff,have_diff)



if __name__ == '__main__':
    a = tmTest('input', 'want', 'have')
        # print(a.read())
    print(a.result())
