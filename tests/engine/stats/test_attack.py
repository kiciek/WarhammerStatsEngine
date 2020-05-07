from unittest import TestCase

from engine.stats.attack import *
from engine.stats.modifiers import ModifierCollection
from engine.stats.units import Unit
from engine.stats.weapons import Weapon


class Test(TestCase):
    # def test_attack_trace(self):
    #     self.fail()

    # def test_attack_sequence_results(self):
    #     self.fail()

    def test_attack_sequence(self):
        weapon = Weapon(
            shots=PMFCollection([PMF.static(1)]),
            strength=4,
            ap=0,
            damage=PMFCollection([PMF.static(1)]),
        )
        target = Unit(
            ws=4,
            bs=4,
            toughness=4,
            save=4,
            invul=7,
            fnp=7,
            wounds=1,
        )
        attacker = Unit(
            ws=4,
            bs=4,
            toughness=4,
            save=4,
            invul=7,
            fnp=7,
            wounds=1,
        )

        mods = ModifierCollection()
        seq = AttackSequence(weapon, target, attacker, mods)
        result = seq.run()
        desired_result = AttackSequenceResults(
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
            PMF.static(0),
        )
        with self.subTest():
            self.assertEqual(result.shot_dist, desired_result.shot_dist)
        with self.subTest():
            self.assertEqual(result.hit_dist, desired_result.hit_dist)
        with self.subTest():
            self.assertEqual(result.wound_dist, desired_result.wound_dist)
        with self.subTest():
            self.assertEqual(result.pen_dist, desired_result.pen_dist)
        with self.subTest():
            self.assertEqual(result.damage_dist, desired_result.damage_dist)
        with self.subTest():
            self.assertEqual(result.drone_wound, desired_result.drone_wound)
        with self.subTest():
            self.assertEqual(result.self_wound, desired_result.self_wound)
        with self.subTest():
            self.assertEqual(result.mortal_dist, desired_result.mortal_dist)
        with self.subTest():
            self.assertEqual(result.damage_with_mortals, desired_result.damage_with_mortals)
    #
    # def test_attack_segment(self):
    #     self.fail()
    #
    # def test_attack_shots(self):
    #     self.fail()
    #
    # def test_attack_hits(self):
    #     self.fail()
    #
    # def test_attack_wounds(self):
    #     self.fail()
    #
    # def test_attack_drones(self):
    #     self.fail()
    #
    # def test_attack_pens(self):
    #     self.fail()
    #
    # def test_attack_damage(self):
    #     self.fail()
