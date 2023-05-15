from django.test import TestCase

# Create your tests here.


def process_branch_name(dat: dict):

    for key, value in dat[0]['filter_obj'].items():
        if "P4WorkSpace" in dat[0]['arges'].keys():
            if key in ["engine_branch", "client_branch"]:
                dat[0]['filter_obj'][key] = value + "(SVN)"

            if key == "content_branch":
                dat[0]['filter_obj'][key] = value + "(P4)"
    return dat



