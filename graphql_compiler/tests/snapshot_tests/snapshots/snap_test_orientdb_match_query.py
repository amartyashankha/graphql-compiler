# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['OrientdbMatchQueryTests::test_immediate_output 1'] = [
    {
        'animal_name': 'Nazgul__(((203)40)(4(204)2)(03(4((203)40)0)))'
    },
    {
        'animal_name': 'Dragon__(2(4(03(013))1)(013))'
    },
    {
        'animal_name': 'Hippogriff__((314)2(312))'
    },
    {
        'animal_name': 'Nazgul__(30(4(204)2))'
    },
    {
        'animal_name': 'Pteranodon__((321)31)'
    },
    {
        'animal_name': 'Hippogriff__4'
    },
    {
        'animal_name': 'Pteranodon__3'
    },
    {
        'animal_name': 'Dragon__1'
    },
    {
        'animal_name': 'Hippogriff__(340)'
    },
    {
        'animal_name': 'Pteranodon__((412)((2(((321)31)2(412))(321))(((321)31)2(412))4)(1((2(((321)31)2(412))(321))(((321)31)2(412))4)(321)))'
    },
    {
        'animal_name': 'Dragon__(304)'
    },
    {
        'animal_name': 'Nazgul__(204)'
    },
    {
        'animal_name': 'Dragon__2'
    },
    {
        'animal_name': 'Hippogriff__0'
    },
    {
        'animal_name': 'Nazgul__1'
    },
    {
        'animal_name': 'Nazgul__(3(203)(1(30(4(204)2))(4((203)40)0)))'
    },
    {
        'animal_name': 'Dragon__((304)(2(4(03(013))1)(013))(20(03(013))))'
    },
    {
        'animal_name': 'Hippogriff__((312)32)'
    },
    {
        'animal_name': 'Nazgul__(4((203)40)0)'
    },
    {
        'animal_name': 'Pteranodon__(((321)31)2(412))'
    },
    {
        'animal_name': 'Hippogriff__(314)'
    },
    {
        'animal_name': 'Pteranodon__4'
    },
    {
        'animal_name': 'Hippogriff__((312)10)'
    },
    {
        'animal_name': 'Pteranodon__(((2(((321)31)2(412))(321))(((321)31)2(412))4)((321)31)4)'
    },
    {
        'animal_name': 'Pteranodon__(2(((321)31)2(412))(321))'
    },
    {
        'animal_name': 'Dragon__(03(013))'
    },
    {
        'animal_name': 'Nazgul__(203)'
    },
    {
        'animal_name': 'Dragon__3'
    },
    {
        'animal_name': 'Hippogriff__1'
    },
    {
        'animal_name': 'Nazgul__2'
    },
    {
        'animal_name': 'Pteranodon__0'
    },
    {
        'animal_name': 'Dragon__(2((304)(2(4(03(013))1)(013))(20(03(013))))(20(03(013))))'
    },
    {
        'animal_name': 'Hippogriff__((314)(312)((312)32))'
    },
    {
        'animal_name': 'Nazgul__(03(4((203)40)0))'
    },
    {
        'animal_name': 'Hippogriff__(2(314)3)'
    },
    {
        'animal_name': 'Pteranodon__(321)'
    },
    {
        'animal_name': 'Pteranodon__1'
    },
    {
        'animal_name': 'Pteranodon__(1(412)((321)31))'
    },
    {
        'animal_name': 'Hippogriff__(3((312)32)(314))'
    },
    {
        'animal_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)'
    },
    {
        'animal_name': 'Dragon__(4(03(013))1)'
    },
    {
        'animal_name': 'Nazgul__((203)40)'
    },
    {
        'animal_name': 'Dragon__4'
    },
    {
        'animal_name': 'Hippogriff__2'
    },
    {
        'animal_name': 'Nazgul__3'
    },
    {
        'animal_name': 'Dragon__(4(2((304)(2(4(03(013))1)(013))(20(03(013))))(20(03(013))))((304)(2(4(03(013))1)(013))(20(03(013)))))'
    },
    {
        'animal_name': 'Nazgul__(1(30(4(204)2))(4((203)40)0))'
    },
    {
        'animal_name': 'Hippogriff__(312)'
    },
    {
        'animal_name': 'Nazgul__(4(204)2)'
    },
    {
        'animal_name': 'Pteranodon__(412)'
    },
    {
        'animal_name': 'Hippogriff__3'
    },
    {
        'animal_name': 'Pteranodon__2'
    },
    {
        'animal_name': 'Dragon__0'
    },
    {
        'animal_name': 'Hippogriff__(((312)32)1((314)(312)((312)32)))'
    },
    {
        'animal_name': 'Pteranodon__(1((2(((321)31)2(412))(321))(((321)31)2(412))4)(321))'
    },
    {
        'animal_name': 'Dragon__(20(03(013)))'
    },
    {
        'animal_name': 'Dragon__(013)'
    },
    {
        'animal_name': 'Nazgul__4'
    },
    {
        'animal_name': 'Dragon__((2(4(03(013))1)(013))(304)(4(03(013))1))'
    },
    {
        'animal_name': 'Nazgul__0'
    }
]

snapshots['OrientdbMatchQueryTests::test_optional_traverse_after_mandatory_traverse 1'] = [
    {
        'child_name': 'Nazgul__((203)40)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(4(204)2)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(03(4((203)40)0))',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Dragon__2',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(4(03(013))1)',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(013)',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Hippogriff__(314)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__2',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__(312)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Nazgul__3',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(4(204)2)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Pteranodon__(321)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__3',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__1',
        'species_name': 'Pteranodon'
    },
    {
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Pteranodon'
    },
    {
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__4',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__0',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Pteranodon__(412)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(1((2(((321)31)2(412))(321))(((321)31)2(412))4)(321))',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Dragon__3',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__0',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__4',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Nazgul__2',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__4',
        'species_name': 'Nazgul'
    },
    {
        'species_name': 'Dragon'
    },
    {
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__3',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(203)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(1(30(4(204)2))(4((203)40)0))',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Dragon__(304)',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(2(4(03(013))1)(013))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(20(03(013)))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Hippogriff__(312)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__2',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Nazgul__4',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__((203)40)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Pteranodon__((321)31)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__2',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(412)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__1',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__4',
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Hippogriff__(312)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__1',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__0',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__((321)31)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__4',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__2',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(((321)31)2(412))',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(321)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Dragon__0',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__3',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(013)',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Nazgul__2',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__3',
        'species_name': 'Nazgul'
    },
    {
        'species_name': 'Dragon'
    },
    {
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Nazgul'
    },
    {
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Dragon__2',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__((304)(2(4(03(013))1)(013))(20(03(013))))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(20(03(013)))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Hippogriff__(314)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__(312)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__((312)32)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__3',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(4((203)40)0)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Hippogriff__2',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__(314)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Pteranodon__3',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__2',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__1',
        'species_name': 'Pteranodon'
    },
    {
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__1',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(412)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__((321)31)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__((312)32)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__(314)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Pteranodon__(2(((321)31)2(412))(321))',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(((321)31)2(412))',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__4',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Dragon__4',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(03(013))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__1',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Nazgul__(203)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__4',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__0',
        'species_name': 'Nazgul'
    },
    {
        'species_name': 'Dragon'
    },
    {
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Dragon__4',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(2((304)(2(4(03(013))1)(013))(20(03(013))))(20(03(013))))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__((304)(2(4(03(013))1)(013))(20(03(013))))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Nazgul__1',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(30(4(204)2))',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(4((203)40)0)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Hippogriff__3',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__1',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__2',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Nazgul__4',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__(204)',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Nazgul__2',
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Pteranodon__4',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__1',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__2',
        'species_name': 'Pteranodon'
    },
    {
        'species_name': 'Hippogriff'
    },
    {
        'species_name': 'Pteranodon'
    },
    {
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Hippogriff__((312)32)',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__1',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Hippogriff__((314)(312)((312)32))',
        'species_name': 'Hippogriff'
    },
    {
        'child_name': 'Pteranodon__1',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Pteranodon__(321)',
        'species_name': 'Pteranodon'
    },
    {
        'child_name': 'Dragon__2',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__0',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(03(013))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__0',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__1',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__3',
        'species_name': 'Dragon'
    },
    {
        'species_name': 'Nazgul'
    },
    {
        'child_name': 'Dragon__(2(4(03(013))1)(013))',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(304)',
        'species_name': 'Dragon'
    },
    {
        'child_name': 'Dragon__(4(03(013))1)',
        'species_name': 'Dragon'
    },
    {
        'species_name': 'Nazgul'
    }
]

snapshots['OrientdbMatchQueryTests::test_traverse_and_output 1'] = [
    {
        'parent_name': 'Nazgul__((203)40)'
    },
    {
        'parent_name': 'Nazgul__(4(204)2)'
    },
    {
        'parent_name': 'Nazgul__(03(4((203)40)0))'
    },
    {
        'parent_name': 'Dragon__2'
    },
    {
        'parent_name': 'Dragon__(4(03(013))1)'
    },
    {
        'parent_name': 'Dragon__(013)'
    },
    {
        'parent_name': 'Hippogriff__(314)'
    },
    {
        'parent_name': 'Hippogriff__2'
    },
    {
        'parent_name': 'Hippogriff__(312)'
    },
    {
        'parent_name': 'Nazgul__3'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Nazgul__(4(204)2)'
    },
    {
        'parent_name': 'Pteranodon__(321)'
    },
    {
        'parent_name': 'Pteranodon__3'
    },
    {
        'parent_name': 'Pteranodon__1'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Hippogriff__4'
    },
    {
        'parent_name': 'Hippogriff__0'
    },
    {
        'parent_name': 'Pteranodon__(412)'
    },
    {
        'parent_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)'
    },
    {
        'parent_name': 'Pteranodon__(1((2(((321)31)2(412))(321))(((321)31)2(412))4)(321))'
    },
    {
        'parent_name': 'Dragon__3'
    },
    {
        'parent_name': 'Dragon__0'
    },
    {
        'parent_name': 'Dragon__4'
    },
    {
        'parent_name': 'Nazgul__2'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Nazgul__4'
    },
    {
        'parent_name': 'Nazgul__3'
    },
    {
        'parent_name': 'Nazgul__(203)'
    },
    {
        'parent_name': 'Nazgul__(1(30(4(204)2))(4((203)40)0))'
    },
    {
        'parent_name': 'Dragon__(304)'
    },
    {
        'parent_name': 'Dragon__(2(4(03(013))1)(013))'
    },
    {
        'parent_name': 'Dragon__(20(03(013)))'
    },
    {
        'parent_name': 'Hippogriff__(312)'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Hippogriff__2'
    },
    {
        'parent_name': 'Nazgul__4'
    },
    {
        'parent_name': 'Nazgul__((203)40)'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Pteranodon__((321)31)'
    },
    {
        'parent_name': 'Pteranodon__2'
    },
    {
        'parent_name': 'Pteranodon__(412)'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Hippogriff__1'
    },
    {
        'parent_name': 'Hippogriff__4'
    },
    {
        'parent_name': 'Hippogriff__(312)'
    },
    {
        'parent_name': 'Hippogriff__1'
    },
    {
        'parent_name': 'Hippogriff__0'
    },
    {
        'parent_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)'
    },
    {
        'parent_name': 'Pteranodon__((321)31)'
    },
    {
        'parent_name': 'Pteranodon__4'
    },
    {
        'parent_name': 'Pteranodon__2'
    },
    {
        'parent_name': 'Pteranodon__(((321)31)2(412))'
    },
    {
        'parent_name': 'Pteranodon__(321)'
    },
    {
        'parent_name': 'Dragon__0'
    },
    {
        'parent_name': 'Dragon__3'
    },
    {
        'parent_name': 'Dragon__(013)'
    },
    {
        'parent_name': 'Nazgul__2'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Nazgul__3'
    },
    {
        'parent_name': 'Dragon__2'
    },
    {
        'parent_name': 'Dragon__((304)(2(4(03(013))1)(013))(20(03(013))))'
    },
    {
        'parent_name': 'Dragon__(20(03(013)))'
    },
    {
        'parent_name': 'Hippogriff__(314)'
    },
    {
        'parent_name': 'Hippogriff__(312)'
    },
    {
        'parent_name': 'Hippogriff__((312)32)'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Nazgul__3'
    },
    {
        'parent_name': 'Nazgul__(4((203)40)0)'
    },
    {
        'parent_name': 'Hippogriff__2'
    },
    {
        'parent_name': 'Hippogriff__(314)'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Pteranodon__3'
    },
    {
        'parent_name': 'Pteranodon__2'
    },
    {
        'parent_name': 'Pteranodon__1'
    },
    {
        'parent_name': 'Pteranodon__1'
    },
    {
        'parent_name': 'Pteranodon__(412)'
    },
    {
        'parent_name': 'Pteranodon__((321)31)'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Hippogriff__((312)32)'
    },
    {
        'parent_name': 'Hippogriff__(314)'
    },
    {
        'parent_name': 'Pteranodon__(2(((321)31)2(412))(321))'
    },
    {
        'parent_name': 'Pteranodon__(((321)31)2(412))'
    },
    {
        'parent_name': 'Pteranodon__4'
    },
    {
        'parent_name': 'Dragon__4'
    },
    {
        'parent_name': 'Dragon__(03(013))'
    },
    {
        'parent_name': 'Dragon__1'
    },
    {
        'parent_name': 'Nazgul__(203)'
    },
    {
        'parent_name': 'Nazgul__4'
    },
    {
        'parent_name': 'Nazgul__0'
    },
    {
        'parent_name': 'Dragon__4'
    },
    {
        'parent_name': 'Dragon__(2((304)(2(4(03(013))1)(013))(20(03(013))))(20(03(013))))'
    },
    {
        'parent_name': 'Dragon__((304)(2(4(03(013))1)(013))(20(03(013))))'
    },
    {
        'parent_name': 'Nazgul__1'
    },
    {
        'parent_name': 'Nazgul__(30(4(204)2))'
    },
    {
        'parent_name': 'Nazgul__(4((203)40)0)'
    },
    {
        'parent_name': 'Hippogriff__3'
    },
    {
        'parent_name': 'Hippogriff__1'
    },
    {
        'parent_name': 'Hippogriff__2'
    },
    {
        'parent_name': 'Nazgul__4'
    },
    {
        'parent_name': 'Nazgul__(204)'
    },
    {
        'parent_name': 'Nazgul__2'
    },
    {
        'parent_name': 'Pteranodon__4'
    },
    {
        'parent_name': 'Pteranodon__1'
    },
    {
        'parent_name': 'Pteranodon__2'
    },
    {
        'parent_name': 'Hippogriff__((312)32)'
    },
    {
        'parent_name': 'Hippogriff__1'
    },
    {
        'parent_name': 'Hippogriff__((314)(312)((312)32))'
    },
    {
        'parent_name': 'Pteranodon__1'
    },
    {
        'parent_name': 'Pteranodon__((2(((321)31)2(412))(321))(((321)31)2(412))4)'
    },
    {
        'parent_name': 'Pteranodon__(321)'
    },
    {
        'parent_name': 'Dragon__2'
    },
    {
        'parent_name': 'Dragon__0'
    },
    {
        'parent_name': 'Dragon__(03(013))'
    },
    {
        'parent_name': 'Dragon__0'
    },
    {
        'parent_name': 'Dragon__1'
    },
    {
        'parent_name': 'Dragon__3'
    },
    {
        'parent_name': 'Dragon__(2(4(03(013))1)(013))'
    },
    {
        'parent_name': 'Dragon__(304)'
    },
    {
        'parent_name': 'Dragon__(4(03(013))1)'
    }
]
