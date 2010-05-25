# Copyright (C) 2010 Kevin Chung <kchungsp93@gmail.com>
#                    Tyler Romeo <tylerromeo@gmail.com>,
#                    Eugene Dobry <edobry@gmail.com>:
#
# This file is part of Kmaps.
#
# Kmaps is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kmaps is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kmaps.  If not, see <http://www.gnu.org/licenses/>.

def cout(message, alert = False):
    global KMAPS_NS
    if KMAPS_NS == "terminal":
        print message
    else:
        print message

def cin(prompt):
    global KMAPS_NS
    if KMAPS_NS == "terminal":
        return raw_input(prompt)
    else:
        return raw_input(prompt)
