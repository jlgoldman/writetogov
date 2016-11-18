import unittest

from api import rep
from logic import rep_service
from testing import test_base

class RepServiceTest(test_base.RealDatabaseTest):
    def service(self):
        return rep_service.RepServiceImpl()

    def test_lookup_py_valid_district_code(self):
        req = rep.LookupRepsRequest(district_code='CA05')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        self.assertEqual('Mike', resp.house_rep.first_name)
        self.assertEqual('Thompson', resp.house_rep.last_name)
        self.assertEqual('HOUSE', resp.house_rep.chamber)
        self.assertEqual('Representative', resp.house_rep.title)
        self.assertEqual('231 Longworth House Office Building Washington DC, 20515', resp.house_rep.address_dc)
        self.assertEqual(['231 Longworth House Office Building', 'Washington DC, 20515'],
            resp.house_rep.address_dc_lines)
        self.assertEqual(rep.Rep.Status.ACTIVE, resp.house_rep.status)
        self.assertEqual('https://writetogov.s3.amazonaws.com/images/rep/127.jpg', resp.house_rep.photo_url)

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('Boxer', senators[0].last_name)
        self.assertEqual('Feinstein', senators[1].last_name)
        self.assertEqual('SENATE', senators[0].chamber)
        self.assertEqual('SENATE', senators[1].chamber)
        self.assertEqual('Senator', senators[0].title)
        self.assertEqual('Senator', senators[1].title)

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)
        self.assertEqual('Senator', leadership[0].title)
        self.assertEqual('Representative', leadership[1].title)

    def test_lookup_py_invalid_district_code_but_valid_state(self):
        req = rep.LookupRepsRequest(district_code='FL99')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('Nelson', senators[0].last_name)
        self.assertEqual('Rubio', senators[1].last_name)
        self.assertEqual('SENATE', senators[0].chamber)
        self.assertEqual('SENATE', senators[1].chamber)

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)

    def test_lookup_py_invalid_district_code_with_invalid_state(self):
        req = rep.LookupRepsRequest(district_code='XY99')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.house_rep)
        self.assertIsNone(resp.senators)
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)

    def test_lookup_py_district_code_with_empty_seat(self):
        req = rep.LookupRepsRequest(district_code='KY01')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        self.assertEqual(None, resp.house_rep.first_name)
        self.assertEqual(None, resp.house_rep.last_name)
        self.assertEqual('HOUSE', resp.house_rep.chamber)

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('McConnell', senators[0].last_name)
        self.assertEqual('Paul', senators[1].last_name)
        self.assertEqual('SENATE', senators[0].chamber)
        self.assertEqual('SENATE', senators[1].chamber)

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)

    def test_lookup_py_valid_latlng(self):
        req = rep.LookupRepsRequest(latlng=rep.LatLng(lat=33.5207, lng=-86.8025))
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        self.assertEqual('Terri', resp.house_rep.first_name)
        self.assertEqual('Sewell', resp.house_rep.last_name)
        self.assertEqual('HOUSE', resp.house_rep.chamber)

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('Sessions', senators[0].last_name)
        self.assertEqual('Shelby', senators[1].last_name)
        self.assertEqual('SENATE', senators[0].chamber)
        self.assertEqual('SENATE', senators[1].chamber)

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)

    def test_lookup_py_invalid_latlng(self):
        req = rep.LookupRepsRequest(latlng=rep.LatLng(lat=51.5074, lng=-0.1278))
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.house_rep)
        self.assertIsNone(resp.senators)
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        leadership = sorted(resp.leadership, key=lambda s: s.last_name)
        self.assertEqual('McConnell', leadership[0].last_name)
        self.assertEqual('Ryan', leadership[1].last_name)
        self.assertEqual('SENATE', leadership[0].chamber)
        self.assertEqual('HOUSE', leadership[1].chamber)

    def test_get_by_rep_ids(self):
        req = rep.GetRepsRequest(rep_ids=[1, 5, 98])
        resp = self.service().invoke('get', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertEqual(3, len(resp.reps))
        reps = sorted(resp.reps, key=lambda r: r.rep_id)
        self.assertEqual(1, reps[0].rep_id)
        self.assertEqual(5, reps[1].rep_id)
        self.assertEqual(98, reps[2].rep_id)

    def test_get_with_invalid_id(self):
        req = rep.GetRepsRequest(rep_ids=[-1])
        resp = self.service().invoke('get', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.reps)

if __name__ == '__main__':
    unittest.main()
