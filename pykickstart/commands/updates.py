#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2007 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc. 
#
from pykickstart.base import *
from pykickstart.errors import *
from pykickstart.options import *

import gettext
_ = lambda x: gettext.ldgettext("pykickstart", x)

class F7_Updates(KickstartCommand):
    removedKeywords = KickstartCommand.removedKeywords
    removedAttrs = KickstartCommand.removedAttrs

    def __init__(self, writePriority=0, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.op = self._getParser()
        self.url = kwargs.get("url", "")

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        if self.url == "floppy":
            retval += "updates\n"
        elif self.url != "":
            retval += "updates %s\n" % self.url

        return retval

    def _getParser(self):
        op = KSOptionParser(lineno=self.lineno)
        return op

    def parse(self, args):
        (opts, extra) = self.op.parse_args(args=args)

        if len(extra) > 1:
            raise KickstartValueError, formatErrorMsg(self.lineno, msg=_("Kickstart command %s only takes one argument") % "updates")
        elif len(extra) == 0:
            self.url = "floppy"
        else:
            self.url = extra[0]

        return self