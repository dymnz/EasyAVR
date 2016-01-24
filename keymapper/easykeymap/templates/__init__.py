# Easy AVR USB Keyboard Firmware Keymapper
# Copyright (C) 2013-2016 David Howland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

max_matrix_dim = 18
max_leds = 12
max_indicators = 8
max_bl_enables = 16

matrix_dims = {
    'COSTAR': (8, 18),
    'TKL': (6, 17),
    'SIXTY': (5, 15),
    'PAD': (6, 6),
    'CARD': (1, 6)
}

macro_lengths = {
    'ATmega32U4': (1024 * 2),
    'ATmega32U2': (1024 * 2),
    'ATmega16U2': (512),
}