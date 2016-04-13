# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import yaml


class State(yaml.YAMLObject):
    @classmethod
    def properties_of_interest(cls, options):
        """Extract the properties concerning this step from the options.

        Note that these options come from the YAML for a given part.
        """

        raise NotImplementedError

    def __init__(self, options):
        self.properties = self.properties_of_interest(options)

    def __repr__(self):
        items = sorted(self.__dict__.items())
        strings = (': '.join((key, repr(value))) for key, value in items)
        representation = ', '.join(strings)

        return '{}({})'.format(self.__class__.__name__, representation)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

        return False