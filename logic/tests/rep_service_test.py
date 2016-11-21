import unittest

from api import rep
from logic import rep_service
from testing import test_base
from testing import test_data

RD = test_data.RepData

class RepServiceTest(test_base.DatabaseWithTestdataTest):
    def service(self):
        return rep_service.RepServiceImpl()

    def test_lookup_py_valid_district_code(self):
        req = rep.LookupRepsRequest(district_code='CA12')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        self.assertEqual('Nancy', resp.house_rep.first_name)
        self.assertEqual('Pelosi', resp.house_rep.last_name)
        self.assertEqual('HOUSE', resp.house_rep.chamber)
        self.assertEqual('Representative', resp.house_rep.title)
        self.assertEqual('233 Longworth House Office Building Washington DC, 20515', resp.house_rep.address_dc)
        self.assertEqual(['233 Longworth House Office Building', 'Washington DC, 20515'],
            resp.house_rep.address_dc_lines)
        self.assertEqual(rep.Rep.Status.ACTIVE, resp.house_rep.status)
        self.assertEqual('https://writetogov.s3.amazonaws.com/images/rep/134.jpg', resp.house_rep.photo_url)

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
        req = rep.LookupRepsRequest(district_code='CA99')
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('Boxer', senators[0].last_name)
        self.assertEqual('Feinstein', senators[1].last_name)
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
        req = rep.LookupRepsRequest(latlng=rep.LatLng(lat=41.1400, lng=-104.8202))
        resp = self.service().invoke('lookup', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNotNone(resp.house_rep)
        self.assertIsNotNone(resp.senators)
        self.assertEqual(2, len(resp.senators))
        self.assertIsNotNone(resp.leadership)
        self.assertEqual(2, len(resp.leadership))

        self.assertEqual('Cynthia', resp.house_rep.first_name)
        self.assertEqual('Lummis', resp.house_rep.last_name)
        self.assertEqual('HOUSE', resp.house_rep.chamber)

        senators = sorted(resp.senators, key=lambda s: s.last_name)
        self.assertEqual('Barrasso', senators[0].last_name)
        self.assertEqual('Enzi', senators[1].last_name)
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
        req = rep.GetRepsRequest(
            rep_ids=[RD.nancy_pelosi.rep_id, RD.cynthia_lummis.rep_id, RD.dianne_feinstein.rep_id])
        resp = self.service().invoke('get', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertEqual(3, len(resp.reps))
        reps = sorted(resp.reps, key=lambda r: r.rep_id)
        self.assertEqual(RD.dianne_feinstein.rep_id, reps[0].rep_id)
        self.assertEqual(RD.nancy_pelosi.rep_id, reps[1].rep_id)
        self.assertEqual(RD.cynthia_lummis.rep_id, reps[2].rep_id)

    def test_get_with_invalid_id(self):
        req = rep.GetRepsRequest(rep_ids=[-1])
        resp = self.service().invoke('get', req)

        self.assertEqual('SUCCESS', resp.response_code)
        self.assertIsNone(resp.reps)

if __name__ == '__main__':
    unittest.main()
