#!/usr/bin/env python3

import argparse
import re
import sys


def is_checked(val: str) -> bool:
    if not val:
        return False
    return val.upper() == 'X'


def is_whitespace(val: str) -> bool:
    pattern = re.compile(r'^\s*$')
    match = pattern.match(val)
    return match is not None


def main(description: str):
    q1_check_pattern = re.compile(r'1\.\s+\[(?P<check>[Xx ]?)\]\s+Is this a new service', re.MULTILINE)
    q1_match = re.search(q1_check_pattern, description)
    if not q1_match:
        raise ValueError('Response to question "Is this a new service?" is missing')

    q2_check_pattern = re.compile(r'2\.\s+\[(?P<check>[Xx ]?)\]\s+Is this change in alignment with the standard.*\\n+(?P<comment>.*)3', re.MULTILINE)
    q2_match = re.search(q2_check_pattern, description)
    if not q2_match:
        raise ValueError('Response to question "Is change in alignment with the standard back-out plan?" is missing')

    q3_check_pattern = re.compile(r'3\.\s+\[(?P<check>[Xx ]?)\]\s+Will this change affect the functionality of the application', re.MULTILINE)
    q3_match = re.search(q3_check_pattern, description)
    if not q3_match:
        raise ValueError('Response to question "Will this change affect the functionality of the application?" is missing')

    q4_check_pattern = re.compile(r'4\.\s+\[(?P<check>[Xx ]?)\]\s+Is there a significant risk of downtime.*\\n+(?P<comment>.*)5', re.MULTILINE)
    q4_match = re.search(q4_check_pattern, description)
    if not q4_match:
        raise ValueError('Response to question "Is there a significant risk of downtime?" is missing')

    q5_check_pattern = re.compile(r'5\.\s+\[(?P<check>[Xx ]?)\]\s+Does this change introduce new/changed dependencies to the application.*\\n+(?P<comment>.*)6', re.MULTILINE)
    q5_match = re.search(q5_check_pattern, description)
    if not q5_match:
        raise ValueError('Response to question "Does this change introduce new/changed dependencies to the application?" is missing')

    q6_check_pattern = re.compile(r'6\.\s+\[(?P<check>[Xx ]?)\]\s+Will this change affect any security controls built into the application.*\\n+(?P<comment>.*)', re.MULTILINE)
    q6_match = re.search(q6_check_pattern, description)
    if not q6_match:
        raise ValueError('Response to question "Will this change affect any security controls built into the application?" is missing')

    if is_checked(q1_match.group('check')):
        # TODO notify InfoSec team here
        sys.exit(0)

    if not is_checked(q2_match.group('check')) and is_whitespace(q2_match.group('comment')):
        raise ValueError('If the change is not in alignment with the standard back-out plan, a new backout plan must be provided')

    if not is_checked(q3_match.group('check')):
        sys.exit(0)

    if is_checked(q4_match.group('check')) and is_whitespace(q4_match.group('comment')):
        raise ValueError('If the change has a significant risk of downtime, details must be provided')

    if is_checked(q5_match.group('check')) and is_whitespace(q5_match.group('comment')):
        raise ValueError('If the change is introducing new or changed dependencies, details must be provided')

    if is_checked(q6_match.group('check')) and is_whitespace(q6_match.group('comment')):
        raise ValueError('If the change affects any security controls, details must be provided')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--description', help='PR Description')

    args = parser.parse_args()

    main(args.description)
