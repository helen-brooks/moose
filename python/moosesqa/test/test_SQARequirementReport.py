#!/usr/bin/env python
#* This file is part of the MOOSE framework
#* https://www.mooseframework.org
#*
#* All rights reserved, see COPYRIGHT for full restrictions
#* https://github.com/idaholab/moose/blob/master/COPYRIGHT
#*
#* Licensed under LGPL 2.1, please see LICENSE for details
#* https://www.gnu.org/licenses/lgpl-2.1.html
import unittest
import mock
import logging
import pyhit
from moosesqa import SQAReport, SQARequirementReport


class TestSQARequirementReport(unittest.TestCase):

    @mock.patch('mooseutils.colorText', side_effect=lambda t, c, **kwargs: t)
    def testBasic(self, color_text):
        reporter = SQARequirementReport(title='moosesqa', directories=['python/moosesqa/test'])
        r = reporter.getReport()
        self.assertEqual(reporter.status, SQAReport.Status.PASS)
        self.assertIn('moosesqa OK', r)

    @mock.patch('mooseutils.colorText', side_effect=lambda t, c, **kwargs: '{}:{}'.format(c,t))
    def testOptions(self, *args):

        reporter = SQARequirementReport(title='testing', specs='spec_missing_req',
                                        directories=['python/moosesqa/test/specs'])
        r = reporter.getReport()
        self.assertEqual(reporter.status, SQAReport.Status.ERROR)
        self.assertIn('log_missing_requirement: 1', r)
        self.assertIn('log_missing_design: 1', r)
        self.assertIn('log_missing_issues: 1', r)
        self.assertIn('log_empty_requirement: 1', r)
        self.assertIn('log_empty_design: 1', r)
        self.assertIn('log_empty_issues: 1',r )

if __name__ == '__main__':
    unittest.main(verbosity=2)
