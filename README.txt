====================
ApprovalTests.Python
====================

Capturing Human Intelligence - ApprovalTests is an open source
assertion/verification library to aid testing.  approvaltests
is the ApprovalTests port for Python.

For more information see: www.approvaltests.com  Typical usage
opten looks like this::

    import unittest
    from approvaltests.Approvals import verify


    class VerifyTests(unittest.TestCase):
        @staticmethod
        def test_verify():
            verify("Hello World.")

