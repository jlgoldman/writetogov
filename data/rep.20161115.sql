--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: rep; Type: TABLE; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE TABLE rep (
    rep_id integer NOT NULL,
    first_name character varying(100),
    last_name character varying(100),
    state_code character varying(2),
    district_number integer,
    district_code character varying(4),
    party_code character varying(1),
    chamber character varying(1),
    email_link character varying(100),
    email character varying(100),
    website character varying(255),
    address_dc character varying(255),
    phone_dc character varying(20),
    bioguide_id character varying(10),
    status character varying(1),
    photo_url character varying(255),
    status_note character varying(100)
);


ALTER TABLE public.rep OWNER TO jonathangoldman;

--
-- Name: rep_rep_id_seq; Type: SEQUENCE; Schema: public; Owner: jonathangoldman
--

CREATE SEQUENCE rep_rep_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rep_rep_id_seq OWNER TO jonathangoldman;

--
-- Name: rep_rep_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jonathangoldman
--

ALTER SEQUENCE rep_rep_id_seq OWNED BY rep.rep_id;


--
-- Name: rep_id; Type: DEFAULT; Schema: public; Owner: jonathangoldman
--

ALTER TABLE ONLY rep ALTER COLUMN rep_id SET DEFAULT nextval('rep_rep_id_seq'::regclass);


--
-- Data for Name: rep; Type: TABLE DATA; Schema: public; Owner: jonathangoldman
--

COPY rep (rep_id, first_name, last_name, state_code, district_number, district_code, party_code, chamber, email_link, email, website, address_dc, phone_dc, bioguide_id, status, photo_url, status_note) FROM stdin;
1	Lamar	Alexander	TN	\N	\N	R	s	http://www.alexander.senate.gov/public/index.cfm?p=Email	\N	http://www.alexander.senate.gov/	455 Dirksen Senate Office Building Washington DC, 20510	(202) 224-4944	A000360	a	http://bioguide.congress.gov/bioguide/photo/A/A000360.jpg	\N
114	Ann	Kirkpatrick	AZ	1	AZ01	D	h	\N	\N	\N	201 Longworth House Office Building Washington DC, 20515	(202) 225-3361	K000368	o	http://bioguide.congress.gov/bioguide/photo/K/K000368.jpg	Running for Senate
146	Lois	Capps	CA	24	CA24	D	h	\N	\N	\N	2231 Rayburn House Office Building Washington DC, 20515	(202) 225-3601	C001036	r	http://bioguide.congress.gov/bioguide/photo/C/C001036.jpg	Announced retirement on April 8, 2015
190	Jeff	Miller	FL	1	FL01	R	h	\N	\N	\N	336 Longworth House Office Building Washington DC, 20515	(202) 225-4136	M001144	r	http://bioguide.congress.gov/bioguide/photo/M/M001144.jpg	Announced retirement on March 10, 2016
191	Gwen	Graham	FL	2	FL02	D	h	\N	\N	\N	1213 Cannon House Office Building Washington DC, 20515	(202) 225-5235	G000575	r	http://bioguide.congress.gov/bioguide/photo/G/G000575.jpg	Announced retirement on April 21, 2016.
193	Ander	Crenshaw	FL	4	FL04	R	h	\N	\N	\N	2161 Rayburn House Office Building Washington DC, 20515	(202) 225-2501	C001045	r	http://bioguide.congress.gov/bioguide/photo/C/C001045.jpg	Announced retirement on April 13, 2016
194	Corrine	Brown	FL	5	FL05	D	h	\N	\N	\N	2111 Rayburn House Office Building Washington DC, 20515	(202) 225-0123	B000911	e	http://bioguide.congress.gov/bioguide/photo/B/B000911.jpg	Lost primary election on Aug. 30, 2016.
195	Ron	DeSantis	FL	6	FL06	R	h	\N	\N	\N	308 Longworth House Office Building Washington DC, 20515	(202) 225-2706	D000621	o	http://bioguide.congress.gov/bioguide/photo/D/D000621.jpg	Running for Senate
198	Alan	Grayson	FL	9	FL09	D	h	\N	\N	\N	303 Longworth House Office Building Washington DC, 20515	(202) 225-9889	G000556	o	http://bioguide.congress.gov/bioguide/photo/G/G000556.jpg	Running for Senate
207	Patrick	Murphy	FL	18	FL18	D	h	\N	\N	\N	211 Longworth House Office Building Washington DC, 20515	(202) 225-3026	M001191	o	http://bioguide.congress.gov/bioguide/photo/M/M001191.jpg	Running for Senate
219	Lynn	Westmoreland	GA	3	GA03	R	h	\N	\N	\N	2202 Rayburn House Office Building Washington DC, 20515	(202) 225-5901	W000796	r	http://bioguide.congress.gov/bioguide/photo/W/W000796.jpg	Announced retirement on Jan. 7, 2016
260	Marlin	Stutzman	IN	3	IN03	R	h	\N	\N	\N	2418 Rayburn House Office Building Washington DC, 20515	(202) 225-4436	S001188	o	http://bioguide.congress.gov/bioguide/photo/S/S001188.jpg	Running for Senate
266	Todd	Young	IN	9	IN09	R	h	\N	\N	\N	1007 Cannon House Office Building Washington DC, 20515	(202) 225-5315	Y000064	o	http://bioguide.congress.gov/bioguide/photo/Y/Y000064.jpg	Running for Senate
267	Tim	Huelskamp	KS	1	KS01	R	h	\N	\N	\N	1110 Cannon House Office Building Washington DC, 20515	(202) 225-2715	H001057	e	http://bioguide.congress.gov/bioguide/photo/H/H001057.jpg	Lost primary election on Aug. 2, 2016.
279	Charles	Boustany	LA	3	LA03	R	h	\N	\N	\N	1431 Cannon House Office Building Washington DC, 20515	(202) 225-2031	B001255	o	http://bioguide.congress.gov/bioguide/photo/B/B001255.jpg	Running for Senate
280	John	Fleming	LA	4	LA04	R	h	\N	\N	\N	2182 Rayburn House Office Building Washington DC, 20515	(202) 225-2777	F000456	o	http://bioguide.congress.gov/bioguide/photo/F/F000456.jpg	Running for Senate
295	Donna	Edwards	MD	4	MD04	D	h	\N	\N	\N	2445 Rayburn House Office Building Washington DC, 20515	(202) 225-8699	E000290	o	http://bioguide.congress.gov/bioguide/photo/E/E000290.jpg	Lost Democratic primary for Senate
299	Chris	Van Hollen	MD	8	MD08	D	h	\N	\N	\N	1707 Cannon House Office Building Washington DC, 20515	(202) 225-5341	V000128	o	http://bioguide.congress.gov/bioguide/photo/V/V000128.jpg	Running for Senate
302	Dan	Benishek	MI	1	MI01	R	h	\N	\N	\N	514 Longworth House Office Building Washington DC, 20515	(202) 225-4735	B001271	r	http://bioguide.congress.gov/bioguide/photo/B/B001271.jpg	Announced retirement on Sept. 17, 2015
311	Candice	Miller	MI	10	MI10	R	h	\N	\N	\N	320 Longworth House Office Building Washington DC, 20515	(202) 225-2106	M001150	r	http://bioguide.congress.gov/bioguide/photo/M/M001150.jpg	Announced retirement on March 6, 2015
317	John	Kline	MN	2	MN02	R	h	\N	\N	\N	2439 Rayburn House Office Building Washington DC, 20515	(202) 225-2271	K000363	r	http://bioguide.congress.gov/bioguide/photo/K/K000363.jpg	Announced retirement on Sept. 3, 2015
339	Renee	Ellmers	NC	2	NC02	R	h	\N	\N	\N	1210 Cannon House Office Building Washington DC, 20515	(202) 225-4531	E000291	e	http://bioguide.congress.gov/bioguide/photo/E/E000291.jpg	Lost primary election.
378	Steve	Israel	NY	3	NY03	D	h	\N	\N	\N	2457 Rayburn House Office Building Washington DC, 20515	(202) 225-3335	I000057	r	http://bioguide.congress.gov/bioguide/photo/I/I000057.jpg	Announced retirement on Jan. 5, 2016
388	Charles	Rangel	NY	13	NY13	D	h	\N	\N	\N	2354 Rayburn House Office Building Washington DC, 20515	(202) 225-4365	R000053	r	http://bioguide.congress.gov/bioguide/photo/R/R000053.jpg	Announced retirement on Oct. 30, 2015
394	Christopher	Gibson	NY	19	NY19	R	h	\N	\N	\N	1708 Cannon House Office Building Washington DC, 20515	(202) 225-5614	G000564	r	http://bioguide.congress.gov/bioguide/photo/G/G000564.jpg	Announced retirement on Jan. 6, 2015
397	Richard	Hanna	NY	22	NY22	R	h	\N	\N	\N	319 Longworth House Office Building Washington DC, 20515	(202) 225-3665	H001051	r	http://bioguide.congress.gov/bioguide/photo/H/H001051.jpg	Announced retirement on Dec. 20, 2015
447	Pedro	Pierluisi	PR	0	PR00	D	h	\N	\N	\N	2410 Rayburn House Office Building Washington DC, 20515	(202) 225-2615	P000596	o	http://bioguide.congress.gov/bioguide/photo/P/P000596.jpg	Running for governor
465	Stephen	Fincher	TN	8	TN08	R	h	\N	\N	\N	2452 Rayburn House Office Building Washington DC, 20515	(202) 225-4714	F000458	r	http://bioguide.congress.gov/bioguide/photo/F/F000458.jpg	Announced retirement on Feb. 1, 2016
481	Rubén	Hinojosa	TX	15	TX15	D	h	\N	\N	\N	2262 Rayburn House Office Building Washington DC, 20515	(202) 225-2531	H000636	r	http://bioguide.congress.gov/bioguide/photo/H/H000636.jpg	Announced retirement on Nov. 13, 2015
485	Randy	Neugebauer	TX	19	TX19	R	h	\N	\N	\N	1424 Cannon House Office Building Washington DC, 20515	(202) 225-4005	N000182	r	http://bioguide.congress.gov/bioguide/photo/N/N000182.jpg	Announced retirement on Sept. 17, 2015
508	E.	Rigell	VA	2	VA02	R	h	\N	\N	\N	418 Longworth House Office Building Washington DC, 20515	(202) 225-4215	R000589	r	http://bioguide.congress.gov/bioguide/photo/R/R000589.jpg	Announced retirement on Jan. 14, 2016
510	J.	Forbes	VA	4	VA04	R	h	\N	\N	\N	2135 Rayburn House Office Building Washington DC, 20515	(202) 225-6365	F000445	e	http://bioguide.congress.gov/bioguide/photo/F/F000445.jpg	Lost primary election.
511	Robert	Hurt	VA	5	VA05	R	h	\N	\N	\N	125 Longworth House Office Building Washington DC, 20515	(202) 225-4711	H001060	r	http://bioguide.congress.gov/bioguide/photo/H/H001060.jpg	Announced retirement on Dec. 23, 2015
526	Jim	McDermott	WA	7	WA07	D	h	\N	\N	\N	1035 Cannon House Office Building Washington DC, 20515	(202) 225-3106	M000404	r	http://bioguide.congress.gov/bioguide/photo/M/M000404.jpg	Announced retirement on Jan. 4, 2016
537	Reid	Ribble	WI	8	WI08	R	h	\N	\N	\N	1513 Cannon House Office Building Washington DC, 20515	(202) 225-5665	R000587	r	http://bioguide.congress.gov/bioguide/photo/R/R000587.jpg	Announced retirement on Jan. 31, 2016
232	\N	\N	HI	1	HI01	\N	h	\N	\N	\N	422 Longworth House Office Building Washington DC, 20515	(202) 225-2726	\N	l	\N	Died on July 20, 2016.
271	\N	\N	KY	1	KY01	\N	h	\N	\N	\N	2184 Rayburn House Office Building Washington DC, 20515	(202) 225-3115	\N	l	\N	Announced resignation effective Sept. 6, 2016.
430	\N	\N	PA	2	PA02	\N	h	\N	\N	\N	2301 Rayburn House Office Building Washington DC, 20515	(202) 225-4001	\N	l	\N	Resigned effective June 23, 2016.
3	Tammy	Baldwin	WI	\N	\N	D	s	https://www.baldwin.senate.gov/feedback	\N	http://www.baldwin.senate.gov/	717 Hart Senate Office Building Washington DC, 20510	(202) 224-5653	B001230	a	http://bioguide.congress.gov/bioguide/photo/B/B001230.jpg	\N
4	John	Barrasso	WY	\N	\N	R	s	https://www.barrasso.senate.gov/public/index.cfm/contact-form	\N	http://www.barrasso.senate.gov	307 Dirksen Senate Office Building Washington DC, 20510	(202) 224-6441	B001261	a	http://bioguide.congress.gov/bioguide/photo/B/B001261.jpg	\N
5	Michael F.	Bennet	CO	\N	\N	D	s	https://www.bennet.senate.gov/?p=contact	\N	http://www.bennet.senate.gov	261 Russell Senate Office Building Washington DC, 20510	(202) 224-5852	B001267	a	http://bioguide.congress.gov/bioguide/photo/B/B001267.jpg	\N
6	Richard	Blumenthal	CT	\N	\N	D	s	https://www.blumenthal.senate.gov/contact/	\N	http://www.blumenthal.senate.gov	706 Hart Senate Office Building Washington DC, 20510	(202) 224-2823	B001277	a	http://bioguide.congress.gov/bioguide/photo/B/B001277.jpg	\N
7	Roy	Blunt	MO	\N	\N	R	s	https://www.blunt.senate.gov/public/index.cfm/contact-roy	\N	http://www.blunt.senate.gov	260 Russell Senate Office Building Washington DC, 20510	(202) 224-5721	B000575	a	http://bioguide.congress.gov/bioguide/photo/B/B000575.jpg	\N
8	Cory A.	Booker	NJ	\N	\N	D	s	https://www.booker.senate.gov/?p=contact	\N	http://www.booker.senate.gov	359 Dirksen Senate Office Building Washington DC, 20510	(202) 224-3224	B001288	a	http://bioguide.congress.gov/bioguide/photo/B/B001288.jpg	\N
9	John	Boozman	AR	\N	\N	R	s	https://www.boozman.senate.gov/public/index.cfm/contact	\N	http://www.boozman.senate.gov/	141 Hart Senate Office Building Washington DC, 20510	(202) 224-4843	B001236	a	http://bioguide.congress.gov/bioguide/photo/B/B001236.jpg	\N
11	Sherrod	Brown	OH	\N	\N	D	s	http://www.brown.senate.gov/contact/	\N	http://www.brown.senate.gov/	713 Hart Senate Office Building Washington DC, 20510	(202) 224-2315	B000944	a	http://bioguide.congress.gov/bioguide/photo/B/B000944.jpg	\N
12	Richard	Burr	NC	\N	\N	R	s	https://www.burr.senate.gov/contact/email	\N	http://www.burr.senate.gov	217 Russell Senate Office Building Washington DC, 20510	(202) 224-3154	B001135	a	http://bioguide.congress.gov/bioguide/photo/B/B001135.jpg	\N
13	Maria	Cantwell	WA	\N	\N	D	s	http://www.cantwell.senate.gov/public/index.cfm/email-maria	\N	http://www.cantwell.senate.gov	511 Hart Senate Office Building Washington DC, 20510	(202) 224-3441	C000127	a	http://bioguide.congress.gov/bioguide/photo/C/C000127.jpg	\N
115	Martha	McSally	AZ	2	AZ02	R	h	\N	\N	\N	1029 Cannon House Office Building Washington DC, 20515	(202) 225-2542	M001197	a	\N	\N
133	Mark	DeSaulnier	CA	11	CA11	D	h	\N	\N	\N	327 Longworth House Office Building Washington DC, 20515	(202) 225-2095	D000623	a	\N	\N
147	Stephen	Knight	CA	25	CA25	R	h	\N	\N	\N	1023 Cannon House Office Building Washington DC, 20515	(202) 225-1956	K000387	a	\N	\N
157	Norma	Torres	CA	35	CA35	D	h	\N	\N	\N	516 Longworth House Office Building Washington DC, 20515	(202) 225-6161	T000474	a	\N	\N
159	Karen	Bass	CA	37	CA37	D	h	\N	\N	\N	408 Longworth House Office Building Washington DC, 20515	(202) 225-7084	B001270	a	\N	\N
189	John	Carney	DE	0	DE00	D	h	\N	\N	\N	1406 Cannon House Office Building Washington DC, 20515	(202) 225-4165	C001083	o	\N	Running for governor
202	David	Jolly	FL	13	FL13	R	h	\N	\N	\N	1728 Cannon House Office Building Washington DC, 20515	(202) 225-5961	J000296	o	\N	Running for Senate
208	Curt	Clawson	FL	19	FL19	R	h	\N	\N	\N	228 Longworth House Office Building Washington DC, 20515	(202) 225-2536	C001102	r	\N	Announced retirement on May 19, 2016.
179	Ken	Buck	CO	4	CO04	R	h	\N	\N	\N	416 Longworth House Office Building Washington DC, 20515	(202) 225-4676	B001297	a	\N	\N
215	Carlos	Curbelo	FL	26	FL26	R	h	\N	\N	\N	1429 Cannon House Office Building Washington DC, 20515	(202) 225-2778	C001107	a	\N	\N
217	Earl	Carter	GA	1	GA01	R	h	\N	\N	\N	432 Longworth House Office Building Washington DC, 20515	(202) 225-5831	C001103	a	\N	\N
257	Darin	LaHood	IL	18	IL18	R	h	\N	\N	\N	2464 Rayburn House Office Building Washington DC, 20515	(202) 225-6201	L000585	l	\N	Announced resignation effective March 31, 2015
227	Barry	Loudermilk	GA	11	GA11	R	h	\N	\N	\N	238 Longworth House Office Building Washington DC, 20515	(202) 225-2931	L000583	a	\N	\N
234	Rod	Blum	IA	1	IA01	R	h	\N	\N	\N	213 Longworth House Office Building Washington DC, 20515	(202) 225-2911	B001294	a	\N	\N
236	David	Young	IA	3	IA03	R	h	\N	\N	\N	515 Longworth House Office Building Washington DC, 20515	(202) 225-5476	Y000066	a	\N	\N
251	Mike	Bost	IL	12	IL12	R	h	\N	\N	\N	1440 Cannon House Office Building Washington DC, 20515	(202) 225-5661	B001295	a	\N	\N
261	Todd	Rokita	IN	4	IN04	R	h	\N	\N	\N	1717 Cannon House Office Building Washington DC, 20515	(202) 225-5037	R000592	a	\N	\N
265	Larry	Bucshon	IN	8	IN08	R	h	\N	\N	\N	1005 Cannon House Office Building Washington DC, 20515	(202) 225-4636	B001275	a	\N	\N
269	Kevin	Yoder	KS	3	KS03	R	h	\N	\N	\N	215 Longworth House Office Building Washington DC, 20515	(202) 225-2865	Y000063	a	\N	\N
333	Trent	Kelly	MS	1	MS01	R	h	\N	\N	\N	1427 Cannon House Office Building Washington DC, 20515	(202) 225-4306	K000388	l	\N	Died on Feb. 6, 2015
282	Garret	Graves	LA	6	LA06	R	h	\N	\N	\N	204 Longworth House Office Building Washington DC, 20515	(202) 225-3901	G000577	a	\N	\N
301	Bruce	Poliquin	ME	2	ME02	R	h	\N	\N	\N	426 Longworth House Office Building Washington DC, 20515	(202) 225-6306	P000611	a	\N	\N
309	Mike	Bishop	MI	8	MI08	R	h	\N	\N	\N	428 Longworth House Office Building Washington DC, 20515	(202) 225-4872	B001293	a	\N	\N
312	David	Trott	MI	11	MI11	R	h	\N	\N	\N	1722 Cannon House Office Building Washington DC, 20515	(202) 225-8171	T000475	a	\N	\N
313	Debbie	Dingell	MI	12	MI12	D	h	\N	\N	\N	116 Longworth House Office Building Washington DC, 20515	(202) 225-4071	D000624	a	\N	\N
315	Brenda	Lawrence	MI	14	MI14	D	h	\N	\N	\N	1237 Cannon House Office Building Washington DC, 20515	(202) 225-5802	L000581	a	\N	\N
321	Tom	Emmer	MN	6	MN06	R	h	\N	\N	\N	503 Longworth House Office Building Washington DC, 20515	(202) 225-2331	E000294	a	\N	\N
386	Daniel	Donovan	NY	11	NY11	R	h	\N	\N	\N	1725 Cannon House Office Building Washington DC, 20515	(202) 225-3371	D000625	l	\N	Resigned from the House on Jan. 5, 2015
337	Ryan	Zinke	MT	0	MT00	R	h	\N	\N	\N	113 Longworth House Office Building Washington DC, 20515	(202) 225-3211	Z000018	a	\N	\N
343	Mark	Walker	NC	6	NC06	R	h	\N	\N	\N	312 Longworth House Office Building Washington DC, 20515	(202) 225-3065	W000819	a	\N	\N
344	David	Rouzer	NC	7	NC07	R	h	\N	\N	\N	424 Longworth House Office Building Washington DC, 20515	(202) 225-2731	R000603	a	\N	\N
349	Alma	Adams	NC	12	NC12	D	h	\N	\N	\N	222 Longworth House Office Building Washington DC, 20515	(202) 225-1510	A000370	a	\N	\N
375	Cresent	Hardy	NV	4	NV04	R	h	\N	\N	\N	430 Longworth House Office Building Washington DC, 20515	(202) 225-9894	H001070	d	\N	\N
376	Lee	Zeldin	NY	1	NY01	R	h	\N	\N	\N	1517 Cannon House Office Building Washington DC, 20515	(202) 225-3826	Z000017	a	\N	\N
410	Warren	Davidson	OH	8	OH08	R	h	\N	\N	\N	1011 Cannon House Office Building Washington DC, 20515	(202) 225-6205	D000626	l	\N	Announced resignation effective Oct. 31, 2015
396	Elise	Stefanik	NY	21	NY21	R	h	\N	\N	\N	512 Longworth House Office Building Washington DC, 20515	(202) 225-4611	S001196	a	\N	\N
399	John	Katko	NY	24	NY24	R	h	\N	\N	\N	1123 Cannon House Office Building Washington DC, 20515	(202) 225-3701	K000386	a	\N	\N
417	Steve	Stivers	OH	15	OH15	R	h	\N	\N	\N	1022 Cannon House Office Building Washington DC, 20515	(202) 225-2015	S001187	a	\N	\N
424	Suzanne	Bonamici	OR	1	OR01	D	h	\N	\N	\N	439 Longworth House Office Building Washington DC, 20515	(202) 225-0855	B001278	a	\N	\N
434	Ryan	Costello	PA	6	PA06	R	h	\N	\N	\N	427 Longworth House Office Building Washington DC, 20515	(202) 225-4315	C001106	a	\N	\N
441	Brendan	Boyle	PA	13	PA13	D	h	\N	\N	\N	118 Longworth House Office Building Washington DC, 20515	(202) 225-6111	B001296	a	\N	\N
448	David	Cicilline	RI	1	RI01	D	h	\N	\N	\N	2244 Rayburn House Office Building Washington DC, 20515	(202) 225-4911	C001084	a	\N	\N
463	Diane	Black	TN	6	TN06	R	h	\N	\N	\N	1131 Cannon House Office Building Washington DC, 20515	(202) 225-4231	B001273	a	\N	\N
470	John	Ratcliffe	TX	4	TX04	R	h	\N	\N	\N	325 Longworth House Office Building Washington DC, 20515	(202) 225-6673	R000601	a	\N	\N
489	Will	Hurd	TX	23	TX23	R	h	\N	\N	\N	317 Longworth House Office Building Washington DC, 20515	(202) 225-4511	H001073	a	\N	\N
506	Mia	Love	UT	4	UT04	R	h	\N	\N	\N	217 Longworth House Office Building Washington DC, 20515	(202) 225-3011	L000584	a	\N	\N
513	Dave	Brat	VA	7	VA07	R	h	\N	\N	\N	330 Longworth House Office Building Washington DC, 20515	(202) 225-2815	B001290	a	\N	\N
516	Barbara	Comstock	VA	10	VA10	R	h	\N	\N	\N	226 Longworth House Office Building Washington DC, 20515	(202) 225-5136	C001105	a	\N	\N
14	Shelley Moore	Capito	WV	\N	\N	R	s	https://www.capito.senate.gov/contact/contact-shelley	\N	http://www.capito.senate.gov	172 Russell Senate Office Building Washington DC, 20510	(202) 224-6472	C001047	a	http://bioguide.congress.gov/bioguide/photo/C/C001047.jpg	\N
15	Benjamin L.	Cardin	MD	\N	\N	D	s	http://www.cardin.senate.gov/contact/	\N	http://www.cardin.senate.gov/	509 Hart Senate Office Building Washington DC, 20510	(202) 224-4524	C000141	a	http://bioguide.congress.gov/bioguide/photo/C/C000141.jpg	\N
16	Thomas R.	Carper	DE	\N	\N	D	s	http://www.carper.senate.gov/public/index.cfm/email-senator-carper	\N	http://www.carper.senate.gov	513 Hart Senate Office Building Washington DC, 20510	(202) 224-2441	C000174	a	http://bioguide.congress.gov/bioguide/photo/C/C000174.jpg	\N
17	Robert P., Jr.	Casey	PA	\N	\N	D	s	https://www.casey.senate.gov/contact/	\N	http://www.casey.senate.gov/	393 Russell Senate Office Building Washington DC, 20510	(202) 224-6324	C001070	a	http://bioguide.congress.gov/bioguide/photo/C/C001070.jpg	\N
2	Kelly	Ayotte	NH	\N	\N	R	s	https://www.ayotte.senate.gov/?p=contact	\N	http://www.ayotte.senate.gov	144 Russell Senate Office Building Washington DC, 20510	(202) 224-3324	A000368	d	http://bioguide.congress.gov/bioguide/photo/A/A000368.jpg	\N
18	Bill	Cassidy	LA	\N	\N	R	s	https://www.cassidy.senate.gov/contact	\N	http://www.cassidy.senate.gov	703 Hart Senate Office Building Washington DC, 20510	(202) 224-5824	C001075	a	http://bioguide.congress.gov/bioguide/photo/C/C001075.jpg	\N
20	Thad	Cochran	MS	\N	\N	R	s	https://www.cochran.senate.gov/public/index.cfm/email-me	\N	http://www.cochran.senate.gov	113 Dirksen Senate Office Building Washington DC, 20510	(202) 224-5054	C000567	a	http://bioguide.congress.gov/bioguide/photo/C/C000567.jpg	\N
21	Susan M.	Collins	ME	\N	\N	R	s	http://www.collins.senate.gov/contact	\N	http://www.collins.senate.gov	413 Dirksen Senate Office Building Washington DC, 20510	(202) 224-2523	C001035	a	http://bioguide.congress.gov/bioguide/photo/C/C001035.jpg	\N
22	Christopher A.	Coons	DE	\N	\N	D	s	https://www.coons.senate.gov/contact	\N	http://www.coons.senate.gov/	127A Russell Senate Office Building Washington DC, 20510	(202) 224-5042	C001088	a	http://bioguide.congress.gov/bioguide/photo/C/C001088.jpg	\N
23	Bob	Corker	TN	\N	\N	R	s	https://www.corker.senate.gov/public/index.cfm/emailme	\N	http://www.corker.senate.gov/	425 Dirksen Senate Office Building Washington DC, 20510	(202) 224-3344	C001071	a	http://bioguide.congress.gov/bioguide/photo/C/C001071.jpg	\N
24	John	Cornyn	TX	\N	\N	R	s	https://www.cornyn.senate.gov/contact	\N	http://www.cornyn.senate.gov/	517 Hart Senate Office Building Washington DC, 20510	(202) 224-2934	C001056	a	http://bioguide.congress.gov/bioguide/photo/C/C001056.jpg	\N
25	Tom	Cotton	AR	\N	\N	R	s	http://www.cotton.senate.gov/?p=contact	\N	http://www.cotton.senate.gov	124 Russell Senate Office Building Washington DC, 20510	(202) 224-2353	C001095	a	http://bioguide.congress.gov/bioguide/photo/C/C001095.jpg	\N
26	Mike	Crapo	ID	\N	\N	R	s	http://www.crapo.senate.gov/contact/email.cfm	\N	http://www.crapo.senate.gov	239 Dirksen Senate Office Building Washington DC, 20510	(202) 224-6142	C000880	a	http://bioguide.congress.gov/bioguide/photo/C/C000880.jpg	\N
27	Ted	Cruz	TX	\N	\N	R	s	http://www.cruz.senate.gov/?p=email_senator	\N	http://www.cruz.senate.gov	404 Russell Senate Office Building Washington DC, 20510	(202) 224-5922	C001098	a	http://bioguide.congress.gov/bioguide/photo/C/C001098.jpg	\N
28	Steve	Daines	MT	\N	\N	R	s	https://www.daines.senate.gov/connect/email-steve	\N	http://www.daines.senate.gov	320 Hart Senate Office Building Washington DC, 20510	(202) 224-2651	D000618	a	http://bioguide.congress.gov/bioguide/photo/D/D000618.jpg	\N
29	Joe	Donnelly	IN	\N	\N	D	s	https://www.donnelly.senate.gov/contact/email-joe	\N	http://www.donnelly.senate.gov	720 Hart Senate Office Building Washington DC, 20510	(202) 224-4814	D000607	a	http://bioguide.congress.gov/bioguide/photo/D/D000607.jpg	\N
30	Richard J.	Durbin	IL	\N	\N	D	s	https://www.durbin.senate.gov/contact/	\N	http://www.durbin.senate.gov	711 Hart Senate Office Building Washington DC, 20510	(202) 224-2152	D000563	a	http://bioguide.congress.gov/bioguide/photo/D/D000563.jpg	\N
31	Michael B.	Enzi	WY	\N	\N	R	s	http://www.enzi.senate.gov/public/index.cfm/contact?p=e-mail-senator-enzi	\N	http://www.enzi.senate.gov	379A Russell Senate Office Building Washington DC, 20510	(202) 224-3424	E000285	a	http://bioguide.congress.gov/bioguide/photo/E/E000285.jpg	\N
32	Joni	Ernst	IA	\N	\N	R	s	https://www.ernst.senate.gov/public/index.cfm/contact	\N	http://www.ernst.senate.gov	111 Russell Senate Office Building Washington DC, 20510	(202) 224-3254	E000295	a	http://bioguide.congress.gov/bioguide/photo/E/E000295.jpg	\N
33	Dianne	Feinstein	CA	\N	\N	D	s	https://www.feinstein.senate.gov/public/index.cfm/e-mail-me	\N	http://www.feinstein.senate.gov	331 Hart Senate Office Building Washington DC, 20510	(202) 224-3841	F000062	a	http://bioguide.congress.gov/bioguide/photo/F/F000062.jpg	\N
34	Deb	Fischer	NE	\N	\N	R	s	http://www.fischer.senate.gov/public/index.cfm/contact	\N	http://www.fischer.senate.gov	454 Russell Senate Office Building Washington DC, 20510	(202) 224-6551	F000463	a	http://bioguide.congress.gov/bioguide/photo/F/F000463.jpg	\N
35	Jeff	Flake	AZ	\N	\N	R	s	https://www.flake.senate.gov/public/index.cfm/contact-jeff	\N	http://www.flake.senate.gov	413 Russell Senate Office Building Washington DC, 20510	(202) 224-4521	F000444	a	http://bioguide.congress.gov/bioguide/photo/F/F000444.jpg	\N
36	Al	Franken	MN	\N	\N	D	s	https://www.franken.senate.gov/?p=contact	\N	http://www.franken.senate.gov	309 Hart Senate Office Building Washington DC, 20510	(202) 224-5641	F000457	a	http://bioguide.congress.gov/bioguide/photo/F/F000457.jpg	\N
37	Cory	Gardner	CO	\N	\N	R	s	https://www.gardner.senate.gov/contact-cory/email-cory	\N	http://www.gardner.senate.gov	354 Russell Senate Office Building Washington DC, 20510	(202) 224-5941	G000562	a	http://bioguide.congress.gov/bioguide/photo/G/G000562.jpg	\N
39	Lindsey	Graham	SC	\N	\N	R	s	https://www.lgraham.senate.gov/public/index.cfm/e-mail-senator-graham	\N	http://www.lgraham.senate.gov/	290 Russell Senate Office Building Washington DC, 20510	(202) 224-5972	G000359	a	http://bioguide.congress.gov/bioguide/photo/G/G000359.jpg	\N
40	Chuck	Grassley	IA	\N	\N	R	s	http://www.grassley.senate.gov/contact	\N	http://www.grassley.senate.gov	135 Hart Senate Office Building Washington DC, 20510	(202) 224-3744	G000386	a	http://bioguide.congress.gov/bioguide/photo/G/G000386.jpg	\N
41	Orrin G.	Hatch	UT	\N	\N	R	s	http://www.hatch.senate.gov/public/index.cfm/contact?p=Email-Orrin	\N	http://www.hatch.senate.gov/	104 Hart Senate Office Building Washington DC, 20510	(202) 224-5251	H000338	a	http://bioguide.congress.gov/bioguide/photo/H/H000338.jpg	\N
42	Martin	Heinrich	NM	\N	\N	D	s	http://www.heinrich.senate.gov/contact	\N	http://www.heinrich.senate.gov/	303 Hart Senate Office Building Washington DC, 20510	(202) 224-5521	H001046	a	http://bioguide.congress.gov/bioguide/photo/H/H001046.jpg	\N
10	Barbara	Boxer	CA	\N	\N	D	s	https://www.boxer.senate.gov/?p=shareyourviews	\N	http://www.boxer.senate.gov	112 Hart Senate Office Building Washington DC, 20510	(202) 224-3553	B000711	r	http://bioguide.congress.gov/bioguide/photo/B/B000711.jpg	Announced retirement on Jan. 8, 2015
19	Daniel	Coats	IN	\N	\N	R	s	http://www.coats.senate.gov/contact/	\N	http://www.coats.senate.gov	493 Russell Senate Office Building Washington DC, 20510	(202) 224-5623	C000542	r	http://bioguide.congress.gov/bioguide/photo/C/C000542.jpg	Announced retirement on March 24, 2015
38	Kirsten E.	Gillibrand	NY	\N	\N	D	s	http://www.gillibrand.senate.gov/contact/	\N	http://www.gillibrand.senate.gov	478 Russell Senate Office Building Washington DC, 20510	(202) 224-4451	G000555	a	http://bioguide.congress.gov/bioguide/photo/G/G000555.jpg	\N
43	Heidi	Heitkamp	ND	\N	\N	D	s	http://www.heitkamp.senate.gov/public/index.cfm/contact	\N	http://www.heitkamp.senate.gov/	110 Hart Senate Office Building Washington DC, 20510	(202) 224-2043	H001069	a	http://bioguide.congress.gov/bioguide/photo/H/H001069.jpg	\N
44	Dean	Heller	NV	\N	\N	R	s	http://www.heller.senate.gov/public/index.cfm/contact-form	\N	http://www.heller.senate.gov/	324 Hart Senate Office Building Washington DC, 20510	(202) 224-6244	H001041	a	http://bioguide.congress.gov/bioguide/photo/H/H001041.jpg	\N
45	Mazie K.	Hirono	HI	\N	\N	D	s	https://www.hirono.senate.gov/contact	\N	http://www.hirono.senate.gov/	330 Hart Senate Office Building Washington DC, 20510	(202) 224-6361	H001042	a	http://bioguide.congress.gov/bioguide/photo/H/H001042.jpg	\N
46	John	Hoeven	ND	\N	\N	R	s	http://www.hoeven.senate.gov/public/index.cfm/email-the-senator	\N	http://www.hoeven.senate.gov	338 Russell Senate Office Building Washington DC, 20510	(202) 224-2551	H001061	a	http://bioguide.congress.gov/bioguide/photo/H/H001061.jpg	\N
47	James M.	Inhofe	OK	\N	\N	R	s	https://www.inhofe.senate.gov/contact	\N	http://www.inhofe.senate.gov/	205 Russell Senate Office Building Washington DC, 20510	(202) 224-4721	I000024	a	http://bioguide.congress.gov/bioguide/photo/I/I000024.jpg	\N
48	Johnny	Isakson	GA	\N	\N	R	s	https://www.isakson.senate.gov/public/index.cfm/email-me	\N	http://www.isakson.senate.gov	131 Russell Senate Office Building Washington DC, 20510	(202) 224-3643	I000055	a	http://bioguide.congress.gov/bioguide/photo/I/I000055.jpg	\N
49	Ron	Johnson	WI	\N	\N	R	s	https://www.ronjohnson.senate.gov/public/index.cfm/email-the-senator	\N	http://www.ronjohnson.senate.gov/	328 Hart Senate Office Building Washington DC, 20510	(202) 224-5323	J000293	a	http://bioguide.congress.gov/bioguide/photo/J/J000293.jpg	\N
50	Tim	Kaine	VA	\N	\N	D	s	https://www.kaine.senate.gov/contact	\N	http://www.kaine.senate.gov/	231 Russell Senate Office Building Washington DC, 20510	(202) 224-4024	K000384	a	http://bioguide.congress.gov/bioguide/photo/K/K000384.jpg	\N
51	Angus S., Jr.	King	ME	\N	\N	I	s	https://www.king.senate.gov/contact	\N	http://www.king.senate.gov/	133 Hart Senate Office Building Washington DC, 20510	(202) 224-5344	K000383	a	http://bioguide.congress.gov/bioguide/photo/K/K000383.jpg	\N
52	Mark	Kirk	IL	\N	\N	R	s	http://www.kirk.senate.gov/?p=contact	\N	http://www.kirk.senate.gov	524 Hart Senate Office Building Washington DC, 20510	(202) 224-2854	K000360	d	http://bioguide.congress.gov/bioguide/photo/K/K000360.jpg	\N
53	Amy	Klobuchar	MN	\N	\N	D	s	http://www.klobuchar.senate.gov/public/contact-amy	\N	http://www.klobuchar.senate.gov/	302 Hart Senate Office Building Washington DC, 20510	(202) 224-3244	K000367	a	http://bioguide.congress.gov/bioguide/photo/K/K000367.jpg	\N
54	James	Lankford	OK	\N	\N	R	s	http://www.lankford.senate.gov/contact/email	\N	http://www.lankford.senate.gov	316 Hart Senate Office Building Washington DC, 20510	(202) 224-5754	L000575	a	http://bioguide.congress.gov/bioguide/photo/L/L000575.jpg	\N
55	Patrick J.	Leahy	VT	\N	\N	D	s	https://www.leahy.senate.gov/contact/	\N	http://www.leahy.senate.gov/	437 Russell Senate Office Building Washington DC, 20510	(202) 224-4242	L000174	a	http://bioguide.congress.gov/bioguide/photo/L/L000174.jpg	\N
56	Mike	Lee	UT	\N	\N	R	s	https://www.lee.senate.gov/public/index.cfm/contact	\N	http://www.lee.senate.gov/	361A Russell Senate Office Building Washington DC, 20510	(202) 224-5444	L000577	a	http://bioguide.congress.gov/bioguide/photo/L/L000577.jpg	\N
57	Joe, III	Manchin	WV	\N	\N	D	s	http://www.manchin.senate.gov/public/index.cfm/contact-form	\N	http://www.manchin.senate.gov/	306 Hart Senate Office Building Washington DC, 20510	(202) 224-3954	M001183	a	http://bioguide.congress.gov/bioguide/photo/M/M001183.jpg	\N
58	Edward J.	Markey	MA	\N	\N	D	s	https://www.markey.senate.gov/contact	\N	http://www.markey.senate.gov/	255 Dirksen Senate Office Building Washington DC, 20510	(202) 224-2742	M000133	a	http://bioguide.congress.gov/bioguide/photo/M/M000133.jpg	\N
59	John	McCain	AZ	\N	\N	R	s	https://www.mccain.senate.gov/public/index.cfm/contact-form	\N	http://www.mccain.senate.gov/	218 Russell Senate Office Building Washington DC, 20510	(202) 224-2235	M000303	a	http://bioguide.congress.gov/bioguide/photo/M/M000303.jpg	\N
60	Claire	McCaskill	MO	\N	\N	D	s	http://www.mccaskill.senate.gov/contact	\N	http://www.mccaskill.senate.gov/	730 Hart Senate Office Building Washington DC, 20510	(202) 224-6154	M001170	a	http://bioguide.congress.gov/bioguide/photo/M/M001170.jpg	\N
61	Mitch	McConnell	KY	\N	\N	R	s	http://www.mcconnell.senate.gov/public/index.cfm?p=contact	\N	http://www.mcconnell.senate.gov/	317 Russell Senate Office Building Washington DC, 20510	(202) 224-2541	M000355	a	http://bioguide.congress.gov/bioguide/photo/M/M000355.jpg	\N
62	Robert	Menendez	NJ	\N	\N	D	s	https://www.menendez.senate.gov/contact	\N	http://www.menendez.senate.gov/	528 Hart Senate Office Building Washington DC, 20510	(202) 224-4744	M000639	a	http://bioguide.congress.gov/bioguide/photo/M/M000639.jpg	\N
63	Jeff	Merkley	OR	\N	\N	D	s	http://www.merkley.senate.gov/contact/	\N	http://www.merkley.senate.gov	313 Hart Senate Office Building Washington DC, 20510	(202) 224-3753	M001176	a	http://bioguide.congress.gov/bioguide/photo/M/M001176.jpg	\N
65	Jerry	Moran	KS	\N	\N	R	s	https://www.moran.senate.gov/public/index.cfm/e-mail-jerry	\N	http://www.moran.senate.gov	521 Dirksen Senate Office Building Washington DC, 20510	(202) 224-6521	M000934	a	http://bioguide.congress.gov/bioguide/photo/M/M000934.jpg	\N
66	Lisa	Murkowski	AK	\N	\N	R	s	https://www.murkowski.senate.gov/public/index.cfm/contact	\N	http://www.murkowski.senate.gov/	709 Hart Senate Office Building Washington DC, 20510	(202) 224-6665	M001153	a	http://bioguide.congress.gov/bioguide/photo/M/M001153.jpg	\N
67	Christopher	Murphy	CT	\N	\N	D	s	http://www.murphy.senate.gov/contact	\N	http://www.murphy.senate.gov/	136 Hart Senate Office Building Washington DC, 20510	(202) 224-4041	M001169	a	http://bioguide.congress.gov/bioguide/photo/M/M001169.jpg	\N
68	Patty	Murray	WA	\N	\N	D	s	http://www.murray.senate.gov/public/index.cfm/contactme	\N	http://www.murray.senate.gov/	154 Russell Senate Office Building Washington DC, 20510	(202) 224-2621	M001111	a	http://bioguide.congress.gov/bioguide/photo/M/M001111.jpg	\N
64	Barbara A.	Mikulski	MD	\N	\N	D	s	http://www.mikulski.senate.gov/contact/	\N	http://www.mikulski.senate.gov/	503 Hart Senate Office Building Washington DC, 20510	(202) 224-4654	M000702	r	http://bioguide.congress.gov/bioguide/photo/M/M000702.jpg	Announced retirement on March 2, 2015
75	Harry	Reid	NV	\N	\N	D	s	http://www.reid.senate.gov/contact	\N	http://www.reid.senate.gov/	522 Hart Senate Office Building Washington DC, 20510	(202) 224-3542	R000146	r	http://bioguide.congress.gov/bioguide/photo/R/R000146.jpg	Announced retirement on March 27, 2015
69	Bill	Nelson	FL	\N	\N	D	s	https://www.billnelson.senate.gov/contact-bill	\N	http://www.billnelson.senate.gov/	716 Hart Senate Office Building Washington DC, 20510	(202) 224-5274	N000032	a	http://bioguide.congress.gov/bioguide/photo/N/N000032.jpg	\N
70	Rand	Paul	KY	\N	\N	R	s	https://www.paul.senate.gov/connect/email-rand	\N	http://www.paul.senate.gov	167 Russell Senate Office Building Washington DC, 20510	(202) 224-4343	P000603	a	http://bioguide.congress.gov/bioguide/photo/P/P000603.jpg	\N
71	David	Perdue	GA	\N	\N	R	s	https://www.perdue.senate.gov/connect/email	\N	http://www.perdue.senate.gov	383 Russell Senate Office Building Washington DC, 20510	(202) 224-3521	P000612	a	http://bioguide.congress.gov/bioguide/photo/P/P000612.jpg	\N
72	Gary C.	Peters	MI	\N	\N	D	s	https://www.peters.senate.gov/contact/email-gary	\N	http://www.peters.senate.gov	724 Hart Senate Office Building Washington DC, 20510	(202) 224-6221	P000595	a	http://bioguide.congress.gov/bioguide/photo/P/P000595.jpg	\N
73	Rob	Portman	OH	\N	\N	R	s	https://www.portman.senate.gov/public/index.cfm/contact?p=contact-form	\N	http://www.portman.senate.gov	448 Russell Senate Office Building Washington DC, 20510	(202) 224-3353	P000449	a	http://bioguide.congress.gov/bioguide/photo/P/P000449.jpg	\N
74	Jack	Reed	RI	\N	\N	D	s	https://www.reed.senate.gov/contact/	\N	http://www.reed.senate.gov/	728 Hart Senate Office Building Washington DC, 20510	(202) 224-4642	R000122	a	http://bioguide.congress.gov/bioguide/photo/R/R000122.jpg	\N
76	James E.	Risch	ID	\N	\N	R	s	http://www.risch.senate.gov/public/index.cfm?p=Email	\N	http://www.risch.senate.gov	483 Russell Senate Office Building Washington DC, 20510	(202) 224-2752	R000584	a	http://bioguide.congress.gov/bioguide/photo/R/R000584.jpg	\N
77	Pat	Roberts	KS	\N	\N	R	s	https://www.roberts.senate.gov/public/?p=EmailPat	\N	http://www.roberts.senate.gov/	109 Hart Senate Office Building Washington DC, 20510	(202) 224-4774	R000307	a	http://bioguide.congress.gov/bioguide/photo/R/R000307.jpg	\N
78	Mike	Rounds	SD	\N	\N	R	s	https://www.rounds.senate.gov/contact/email-mike	\N	http://www.rounds.senate.gov	502 Hart Senate Office Building Washington DC, 20510	(202) 224-5842	R000605	a	http://bioguide.congress.gov/bioguide/photo/R/R000605.jpg	\N
79	Marco	Rubio	FL	\N	\N	R	s	http://www.rubio.senate.gov/public/index.cfm/contact	\N	http://www.rubio.senate.gov	284 Russell Senate Office Building Washington DC, 20510	(202) 224-3041	R000595	a	http://bioguide.congress.gov/bioguide/photo/R/R000595.jpg	\N
80	Bernard	Sanders	VT	\N	\N	I	s	http://www.sanders.senate.gov/contact/	\N	http://www.sanders.senate.gov/	332 Dirksen Senate Office Building Washington DC, 20510	(202) 224-5141	S000033	a	http://bioguide.congress.gov/bioguide/photo/S/S000033.jpg	\N
81	Ben	Sasse	NE	\N	\N	R	s	http://www.sasse.senate.gov/public/index.cfm/email-ben	\N	http://www.sasse.senate.gov	386A Russell Senate Office Building Washington DC, 20510	(202) 224-4224	S001197	a	http://bioguide.congress.gov/bioguide/photo/S/S001197.jpg	\N
82	Brian	Schatz	HI	\N	\N	D	s	https://www.schatz.senate.gov/contact	\N	http://www.schatz.senate.gov	722 Hart Senate Office Building Washington DC, 20510	(202) 224-3934	S001194	a	http://bioguide.congress.gov/bioguide/photo/S/S001194.jpg	\N
83	Charles E.	Schumer	NY	\N	\N	D	s	https://www.schumer.senate.gov/contact/email-chuck	\N	http://www.schumer.senate.gov/	322 Hart Senate Office Building Washington DC, 20510	(202) 224-6542	S000148	a	http://bioguide.congress.gov/bioguide/photo/S/S000148.jpg	\N
84	Tim	Scott	SC	\N	\N	R	s	https://www.scott.senate.gov/contact/email-me	\N	http://www.scott.senate.gov/	520 Hart Senate Office Building Washington DC, 20510	(202) 224-6121	S001184	a	http://bioguide.congress.gov/bioguide/photo/S/S001184.jpg	\N
85	Jeff	Sessions	AL	\N	\N	R	s	http://www.sessions.senate.gov/public/index.cfm/contact-jeff	\N	http://www.sessions.senate.gov/	326 Russell Senate Office Building Washington DC, 20510	(202) 224-4124	S001141	a	http://bioguide.congress.gov/bioguide/photo/S/S001141.jpg	\N
86	Jeanne	Shaheen	NH	\N	\N	D	s	http://www.shaheen.senate.gov/contact/	\N	http://www.shaheen.senate.gov	506 Hart Senate Office Building Washington DC, 20510	(202) 224-2841	S001181	a	http://bioguide.congress.gov/bioguide/photo/S/S001181.jpg	\N
87	Richard C.	Shelby	AL	\N	\N	R	s	https://www.shelby.senate.gov/public/index.cfm/emailsenatorshelby	\N	http://www.shelby.senate.gov/	304 Russell Senate Office Building Washington DC, 20510	(202) 224-5744	S000320	a	http://bioguide.congress.gov/bioguide/photo/S/S000320.jpg	\N
88	Debbie	Stabenow	MI	\N	\N	D	s	http://www.stabenow.senate.gov/?p=contact	\N	http://www.stabenow.senate.gov/	731 Hart Senate Office Building Washington DC, 20510	(202) 224-4822	S000770	a	http://bioguide.congress.gov/bioguide/photo/S/S000770.jpg	\N
89	Daniel	Sullivan	AK	\N	\N	R	s	https://www.sullivan.senate.gov/contact/email	\N	http://www.sullivan.senate.gov	702 Hart Senate Office Building Washington DC, 20510	(202) 224-3004	S001198	a	http://bioguide.congress.gov/bioguide/photo/S/S001198.jpg	\N
90	Jon	Tester	MT	\N	\N	D	s	https://www.tester.senate.gov/?p=email_senator	\N	http://www.tester.senate.gov/	311 Hart Senate Office Building Washington DC, 20510	(202) 224-2644	T000464	a	http://bioguide.congress.gov/bioguide/photo/T/T000464.jpg	\N
91	John	Thune	SD	\N	\N	R	s	http://www.thune.senate.gov/public/index.cfm/contact	\N	http://www.thune.senate.gov/	511 Dirksen Senate Office Building Washington DC, 20510	(202) 224-2321	T000250	a	http://bioguide.congress.gov/bioguide/photo/T/T000250.jpg	\N
92	Thom	Tillis	NC	\N	\N	R	s	https://www.tillis.senate.gov/public/index.cfm/email-me	\N	http://www.tillis.senate.gov	185 Dirksen Senate Office Building Washington DC, 20510	(202) 224-6342	T000476	a	http://bioguide.congress.gov/bioguide/photo/T/T000476.jpg	\N
93	Patrick J.	Toomey	PA	\N	\N	R	s	https://www.toomey.senate.gov/?p=contact	\N	http://www.toomey.senate.gov/	248 Russell Senate Office Building Washington DC, 20510	(202) 224-4254	T000461	a	http://bioguide.congress.gov/bioguide/photo/T/T000461.jpg	\N
94	Tom	Udall	NM	\N	\N	D	s	https://www.tomudall.senate.gov/?p=contact	\N	http://www.tomudall.senate.gov	531 Hart Senate Office Building Washington DC, 20510	(202) 224-6621	U000039	a	http://bioguide.congress.gov/bioguide/photo/U/U000039.jpg	\N
96	Mark R.	Warner	VA	\N	\N	D	s	http://www.warner.senate.gov/public/index.cfm?p=Contact	\N	http://www.warner.senate.gov	475 Russell Senate Office Building Washington DC, 20510	(202) 224-2023	W000805	a	http://bioguide.congress.gov/bioguide/photo/W/W000805.jpg	\N
97	Elizabeth	Warren	MA	\N	\N	D	s	https://www.warren.senate.gov/?p=email_senator	\N	http://www.warren.senate.gov	317 Hart Senate Office Building Washington DC, 20510	(202) 224-4543	W000817	a	http://bioguide.congress.gov/bioguide/photo/W/W000817.jpg	\N
98	Sheldon	Whitehouse	RI	\N	\N	D	s	https://www.whitehouse.senate.gov/contact/	\N	http://www.whitehouse.senate.gov/	530 Hart Senate Office Building Washington DC, 20510	(202) 224-2921	W000802	a	http://bioguide.congress.gov/bioguide/photo/W/W000802.jpg	\N
99	Roger F.	Wicker	MS	\N	\N	R	s	https://www.wicker.senate.gov/public/index.cfm/contact	\N	http://www.wicker.senate.gov	555 Dirksen Senate Office Building Washington DC, 20510	(202) 224-6253	W000437	a	http://bioguide.congress.gov/bioguide/photo/W/W000437.jpg	\N
100	Ron	Wyden	OR	\N	\N	D	s	https://www.wyden.senate.gov/contact/	\N	http://www.wyden.senate.gov/	221 Dirksen Senate Office Building Washington DC, 20510	(202) 224-5244	W000779	a	http://bioguide.congress.gov/bioguide/photo/W/W000779.jpg	\N
95	David	Vitter	LA	\N	\N	R	s	http://www.vitter.senate.gov/contact	\N	http://www.vitter.senate.gov/	516 Hart Senate Office Building Washington DC, 20510	(202) 224-4623	V000127	r	http://bioguide.congress.gov/bioguide/photo/V/V000127.jpg	Announced retirement on Nov. 21, 2015
101	Don	Young	AK	0	AK00	R	h	\N	\N	\N	2314 Rayburn House Office Building Washington DC, 20515	(202) 225-5765	Y000033	a	http://bioguide.congress.gov/bioguide/photo/Y/Y000033.jpg	\N
102	Bradley	Byrne	AL	1	AL01	R	h	\N	\N	\N	119 Longworth House Office Building Washington DC, 20515	(202) 225-4931	B001289	a	http://bioguide.congress.gov/bioguide/photo/B/B001289.jpg	\N
103	Martha	Roby	AL	2	AL02	R	h	\N	\N	\N	442 Longworth House Office Building Washington DC, 20515	(202) 225-2901	R000591	a	http://bioguide.congress.gov/bioguide/photo/R/R000591.jpg	\N
104	Mike	Rogers	AL	3	AL03	R	h	\N	\N	\N	324 Longworth House Office Building Washington DC, 20515	(202) 225-3261	R000575	a	http://bioguide.congress.gov/bioguide/photo/R/R000575.jpg	\N
105	Robert	Aderholt	AL	4	AL04	R	h	\N	\N	\N	235 Longworth House Office Building Washington DC, 20515	(202) 225-4876	A000055	a	http://bioguide.congress.gov/bioguide/photo/A/A000055.jpg	\N
106	Mo	Brooks	AL	5	AL05	R	h	\N	\N	\N	1230 Cannon House Office Building Washington DC, 20515	(202) 225-4801	B001274	a	http://bioguide.congress.gov/bioguide/photo/B/B001274.jpg	\N
107	Gary	Palmer	AL	6	AL06	R	h	\N	\N	\N	206 Longworth House Office Building Washington DC, 20515	(202) 225-4921	P000609	a	http://bioguide.congress.gov/bioguide/photo/P/P000609.jpg	\N
108	Terri	Sewell	AL	7	AL07	D	h	\N	\N	\N	1133 Cannon House Office Building Washington DC, 20515	(202) 225-2665	S001185	a	http://bioguide.congress.gov/bioguide/photo/S/S001185.jpg	\N
109	Eric	Crawford	AR	1	AR01	R	h	\N	\N	\N	1711 Cannon House Office Building Washington DC, 20515	(202) 225-4076	C001087	a	http://bioguide.congress.gov/bioguide/photo/C/C001087.jpg	\N
110	J.	Hill	AR	2	AR02	R	h	\N	\N	\N	1229 Cannon House Office Building Washington DC, 20515	(202) 225-2506	H001072	a	http://bioguide.congress.gov/bioguide/photo/H/H001072.jpg	\N
111	Steve	Womack	AR	3	AR03	R	h	\N	\N	\N	1119 Cannon House Office Building Washington DC, 20515	(202) 225-4301	W000809	a	http://bioguide.congress.gov/bioguide/photo/W/W000809.jpg	\N
112	Bruce	Westerman	AR	4	AR04	R	h	\N	\N	\N	130 Longworth House Office Building Washington DC, 20515	(202) 225-3772	W000821	a	http://bioguide.congress.gov/bioguide/photo/W/W000821.jpg	\N
113	Aumua Amata	Radewagen	AS	0	AQ00	R	h	\N	\N	\N	1339 Cannon House Office Building Washington DC, 20515	(202) 225-8577	R000600	a	http://bioguide.congress.gov/bioguide/photo/R/R000600.jpg	\N
116	Raúl	Grijalva	AZ	3	AZ03	D	h	\N	\N	\N	1511 Cannon House Office Building Washington DC, 20515	(202) 225-2435	G000551	a	http://bioguide.congress.gov/bioguide/photo/G/G000551.jpg	\N
117	Paul	Gosar	AZ	4	AZ04	R	h	\N	\N	\N	504 Longworth House Office Building Washington DC, 20515	(202) 225-2315	G000565	a	http://bioguide.congress.gov/bioguide/photo/G/G000565.jpg	\N
119	David	Schweikert	AZ	6	AZ06	R	h	\N	\N	\N	409 Longworth House Office Building Washington DC, 20515	(202) 225-2190	S001183	a	http://bioguide.congress.gov/bioguide/photo/S/S001183.jpg	\N
120	Ruben	Gallego	AZ	7	AZ07	D	h	\N	\N	\N	1218 Cannon House Office Building Washington DC, 20515	(202) 225-4065	G000574	a	http://bioguide.congress.gov/bioguide/photo/G/G000574.jpg	\N
129	Ami	Bera	CA	7	CA07	D	h	\N	\N	\N	1535 Cannon House Office Building Washington DC, 20515	(202) 225-5716	B001287	p	http://bioguide.congress.gov/bioguide/photo/B/B001287.jpg	\N
118	Matt	Salmon	AZ	5	AZ05	R	h	\N	\N	\N	2349 Rayburn House Office Building Washington DC, 20515	(202) 225-2635	S000018	r	http://bioguide.congress.gov/bioguide/photo/S/S000018.jpg	Announced retirement on February 25, 2016
142	Sam	Farr	CA	20	CA20	D	h	\N	\N	\N	1126 Cannon House Office Building Washington DC, 20515	(202) 225-2861	F000030	r	http://bioguide.congress.gov/bioguide/photo/F/F000030.jpg	Announced retirement on Nov. 12, 2015
121	Trent	Franks	AZ	8	AZ08	R	h	\N	\N	\N	2435 Rayburn House Office Building Washington DC, 20515	(202) 225-4576	F000448	a	http://bioguide.congress.gov/bioguide/photo/F/F000448.jpg	\N
122	Kyrsten	Sinema	AZ	9	AZ09	D	h	\N	\N	\N	1530 Cannon House Office Building Washington DC, 20515	(202) 225-9888	S001191	a	http://bioguide.congress.gov/bioguide/photo/S/S001191.jpg	\N
123	Doug	LaMalfa	CA	1	CA01	R	h	\N	\N	\N	322 Longworth House Office Building Washington DC, 20515	(202) 225-3076	L000578	a	http://bioguide.congress.gov/bioguide/photo/L/L000578.jpg	\N
124	Jared	Huffman	CA	2	CA02	D	h	\N	\N	\N	1630 Cannon House Office Building Washington DC, 20515	(202) 225-5161	H001068	a	http://bioguide.congress.gov/bioguide/photo/H/H001068.jpg	\N
125	John	Garamendi	CA	3	CA03	D	h	\N	\N	\N	2438 Rayburn House Office Building Washington DC, 20515	(202) 225-1880	G000559	a	http://bioguide.congress.gov/bioguide/photo/G/G000559.jpg	\N
126	Tom	McClintock	CA	4	CA04	R	h	\N	\N	\N	2331 Rayburn House Office Building Washington DC, 20515	(202) 225-2511	M001177	a	http://bioguide.congress.gov/bioguide/photo/M/M001177.jpg	\N
127	Mike	Thompson	CA	5	CA05	D	h	\N	\N	\N	231 Longworth House Office Building Washington DC, 20515	(202) 225-3311	T000460	a	http://bioguide.congress.gov/bioguide/photo/T/T000460.jpg	\N
128	Doris	Matsui	CA	6	CA06	D	h	\N	\N	\N	2311 Rayburn House Office Building Washington DC, 20515	(202) 225-7163	M001163	a	http://bioguide.congress.gov/bioguide/photo/M/M001163.jpg	\N
130	Paul	Cook	CA	8	CA08	R	h	\N	\N	\N	1222 Cannon House Office Building Washington DC, 20515	(202) 225-5861	C001094	a	http://bioguide.congress.gov/bioguide/photo/C/C001094.jpg	\N
131	Jerry	McNerney	CA	9	CA09	D	h	\N	\N	\N	2265 Rayburn House Office Building Washington DC, 20515	(202) 225-1947	M001166	a	http://bioguide.congress.gov/bioguide/photo/M/M001166.jpg	\N
132	Jeff	Denham	CA	10	CA10	R	h	\N	\N	\N	1730 Cannon House Office Building Washington DC, 20515	(202) 225-4540	D000612	a	http://bioguide.congress.gov/bioguide/photo/D/D000612.jpg	\N
134	Nancy	Pelosi	CA	12	CA12	D	h	\N	\N	\N	233 Longworth House Office Building Washington DC, 20515	(202) 225-4965	P000197	a	http://bioguide.congress.gov/bioguide/photo/P/P000197.jpg	\N
135	Barbara	Lee	CA	13	CA13	D	h	\N	\N	\N	2267 Rayburn House Office Building Washington DC, 20515	(202) 225-2661	L000551	a	http://bioguide.congress.gov/bioguide/photo/L/L000551.jpg	\N
136	Jackie	Speier	CA	14	CA14	D	h	\N	\N	\N	2465 Rayburn House Office Building Washington DC, 20515	(202) 225-3531	S001175	a	http://bioguide.congress.gov/bioguide/photo/S/S001175.jpg	\N
137	Eric	Swalwell	CA	15	CA15	D	h	\N	\N	\N	129 Longworth House Office Building Washington DC, 20515	(202) 225-5065	S001193	a	http://bioguide.congress.gov/bioguide/photo/S/S001193.jpg	\N
138	Jim	Costa	CA	16	CA16	D	h	\N	\N	\N	1314 Cannon House Office Building Washington DC, 20515	(202) 225-3341	C001059	a	http://bioguide.congress.gov/bioguide/photo/C/C001059.jpg	\N
139	Michael	Honda	CA	17	CA17	D	h	\N	\N	\N	1713 Cannon House Office Building Washington DC, 20515	(202) 225-2631	H001034	d	http://bioguide.congress.gov/bioguide/photo/H/H001034.jpg	\N
140	Anna	Eshoo	CA	18	CA18	D	h	\N	\N	\N	241 Longworth House Office Building Washington DC, 20515	(202) 225-8104	E000215	a	http://bioguide.congress.gov/bioguide/photo/E/E000215.jpg	\N
141	Zoe	Lofgren	CA	19	CA19	D	h	\N	\N	\N	1401 Cannon House Office Building Washington DC, 20515	(202) 225-3072	L000397	a	http://bioguide.congress.gov/bioguide/photo/L/L000397.jpg	\N
143	David	Valadao	CA	21	CA21	R	h	\N	\N	\N	1004 Cannon House Office Building Washington DC, 20515	(202) 225-4695	V000129	a	http://bioguide.congress.gov/bioguide/photo/V/V000129.jpg	\N
144	Devin	Nunes	CA	22	CA22	R	h	\N	\N	\N	1013 Cannon House Office Building Washington DC, 20515	(202) 225-2523	N000181	a	http://bioguide.congress.gov/bioguide/photo/N/N000181.jpg	\N
145	Kevin	McCarthy	CA	23	CA23	R	h	\N	\N	\N	2421 Rayburn House Office Building Washington DC, 20515	(202) 225-2915	M001165	a	http://bioguide.congress.gov/bioguide/photo/M/M001165.jpg	\N
148	Julia	Brownley	CA	26	CA26	D	h	\N	\N	\N	1019 Cannon House Office Building Washington DC, 20515	(202) 225-5811	B001285	a	http://bioguide.congress.gov/bioguide/photo/B/B001285.jpg	\N
149	Judy	Chu	CA	27	CA27	D	h	\N	\N	\N	2423 Rayburn House Office Building Washington DC, 20515	(202) 225-5464	C001080	a	http://bioguide.congress.gov/bioguide/photo/C/C001080.jpg	\N
150	Adam	Schiff	CA	28	CA28	D	h	\N	\N	\N	2411 Rayburn House Office Building Washington DC, 20515	(202) 225-4176	S001150	a	http://bioguide.congress.gov/bioguide/photo/S/S001150.jpg	\N
151	Tony	Cárdenas	CA	29	CA29	D	h	\N	\N	\N	1510 Cannon House Office Building Washington DC, 20515	(202) 225-6131	C001097	a	http://bioguide.congress.gov/bioguide/photo/C/C001097.jpg	\N
152	Brad	Sherman	CA	30	CA30	D	h	\N	\N	\N	2242 Rayburn House Office Building Washington DC, 20515	(202) 225-5911	S000344	a	http://bioguide.congress.gov/bioguide/photo/S/S000344.jpg	\N
153	Pete	Aguilar	CA	31	CA31	D	h	\N	\N	\N	1223 Cannon House Office Building Washington DC, 20515	(202) 225-3201	A000371	a	http://bioguide.congress.gov/bioguide/photo/A/A000371.jpg	\N
154	Grace	Napolitano	CA	32	CA32	D	h	\N	\N	\N	1610 Cannon House Office Building Washington DC, 20515	(202) 225-5256	N000179	a	http://bioguide.congress.gov/bioguide/photo/N/N000179.jpg	\N
155	Ted	Lieu	CA	33	CA33	D	h	\N	\N	\N	415 Longworth House Office Building Washington DC, 20515	(202) 225-3976	L000582	a	http://bioguide.congress.gov/bioguide/photo/L/L000582.jpg	\N
156	Xavier	Becerra	CA	34	CA34	D	h	\N	\N	\N	1226 Cannon House Office Building Washington DC, 20515	(202) 225-6235	B000287	a	http://bioguide.congress.gov/bioguide/photo/B/B000287.jpg	\N
158	Raul	Ruiz	CA	36	CA36	D	h	\N	\N	\N	1319 Cannon House Office Building Washington DC, 20515	(202) 225-5330	R000599	a	http://bioguide.congress.gov/bioguide/photo/R/R000599.jpg	\N
160	Linda	Sánchez	CA	38	CA38	D	h	\N	\N	\N	2329 Rayburn House Office Building Washington DC, 20515	(202) 225-6676	S001156	a	http://bioguide.congress.gov/bioguide/photo/S/S001156.jpg	\N
171	Darrell	Issa	CA	49	CA49	R	h	\N	\N	\N	2269 Rayburn House Office Building Washington DC, 20515	(202) 225-3906	I000056	p	http://bioguide.congress.gov/bioguide/photo/I/I000056.jpg	\N
166	Janice	Hahn	CA	44	CA44	D	h	\N	\N	\N	404 Longworth House Office Building Washington DC, 20515	(202) 225-8220	H001063	o	http://bioguide.congress.gov/bioguide/photo/H/H001063.jpg	Running for county supervisor
161	Edward	Royce	CA	39	CA39	R	h	\N	\N	\N	2310 Rayburn House Office Building Washington DC, 20515	(202) 225-4111	R000487	a	http://bioguide.congress.gov/bioguide/photo/R/R000487.jpg	\N
162	Lucille	Roybal-Allard	CA	40	CA40	D	h	\N	\N	\N	2330 Rayburn House Office Building Washington DC, 20515	(202) 225-1766	R000486	a	http://bioguide.congress.gov/bioguide/photo/R/R000486.jpg	\N
163	Mark	Takano	CA	41	CA41	D	h	\N	\N	\N	1507 Cannon House Office Building Washington DC, 20515	(202) 225-2305	T000472	a	http://bioguide.congress.gov/bioguide/photo/T/T000472.jpg	\N
164	Ken	Calvert	CA	42	CA42	R	h	\N	\N	\N	2205 Rayburn House Office Building Washington DC, 20515	(202) 225-1986	C000059	a	http://bioguide.congress.gov/bioguide/photo/C/C000059.jpg	\N
165	Maxine	Waters	CA	43	CA43	D	h	\N	\N	\N	2221 Rayburn House Office Building Washington DC, 20515	(202) 225-2201	W000187	a	http://bioguide.congress.gov/bioguide/photo/W/W000187.jpg	\N
167	Mimi	Walters	CA	45	CA45	R	h	\N	\N	\N	236 Longworth House Office Building Washington DC, 20515	(202) 225-5611	W000820	a	http://bioguide.congress.gov/bioguide/photo/W/W000820.jpg	\N
169	Alan	Lowenthal	CA	47	CA47	D	h	\N	\N	\N	108 Longworth House Office Building Washington DC, 20515	(202) 225-7924	L000579	a	http://bioguide.congress.gov/bioguide/photo/L/L000579.jpg	\N
168	Loretta	Sanchez	CA	46	CA46	D	h	\N	\N	\N	1211 Cannon House Office Building Washington DC, 20515	(202) 225-2965	S000030	o	http://bioguide.congress.gov/bioguide/photo/S/S000030.jpg	Running for Senate
170	Dana	Rohrabacher	CA	48	CA48	R	h	\N	\N	\N	2300 Rayburn House Office Building Washington DC, 20515	(202) 225-2415	R000409	a	http://bioguide.congress.gov/bioguide/photo/R/R000409.jpg	\N
172	Duncan	Hunter	CA	50	CA50	R	h	\N	\N	\N	2429 Rayburn House Office Building Washington DC, 20515	(202) 225-5672	H001048	a	http://bioguide.congress.gov/bioguide/photo/H/H001048.jpg	\N
173	Juan	Vargas	CA	51	CA51	D	h	\N	\N	\N	1605 Cannon House Office Building Washington DC, 20515	(202) 225-8045	V000130	a	http://bioguide.congress.gov/bioguide/photo/V/V000130.jpg	\N
174	Scott	Peters	CA	52	CA52	D	h	\N	\N	\N	1122 Cannon House Office Building Washington DC, 20515	(202) 225-0508	P000608	a	http://bioguide.congress.gov/bioguide/photo/P/P000608.jpg	\N
175	Susan	Davis	CA	53	CA53	D	h	\N	\N	\N	1214 Cannon House Office Building Washington DC, 20515	(202) 225-2040	D000598	a	http://bioguide.congress.gov/bioguide/photo/D/D000598.jpg	\N
176	Diana	DeGette	CO	1	CO01	D	h	\N	\N	\N	2368 Rayburn House Office Building Washington DC, 20515	(202) 225-4431	D000197	a	http://bioguide.congress.gov/bioguide/photo/D/D000197.jpg	\N
177	Jared	Polis	CO	2	CO02	D	h	\N	\N	\N	1433 Cannon House Office Building Washington DC, 20515	(202) 225-2161	P000598	a	http://bioguide.congress.gov/bioguide/photo/P/P000598.jpg	\N
178	Scott	Tipton	CO	3	CO03	R	h	\N	\N	\N	218 Longworth House Office Building Washington DC, 20515	(202) 225-4761	T000470	a	http://bioguide.congress.gov/bioguide/photo/T/T000470.jpg	\N
180	Doug	Lamborn	CO	5	CO05	R	h	\N	\N	\N	2402 Rayburn House Office Building Washington DC, 20515	(202) 225-4422	L000564	a	http://bioguide.congress.gov/bioguide/photo/L/L000564.jpg	\N
181	Mike	Coffman	CO	6	CO06	R	h	\N	\N	\N	2443 Rayburn House Office Building Washington DC, 20515	(202) 225-7882	C001077	a	http://bioguide.congress.gov/bioguide/photo/C/C001077.jpg	\N
182	Ed	Perlmutter	CO	7	CO07	D	h	\N	\N	\N	1410 Cannon House Office Building Washington DC, 20515	(202) 225-2645	P000593	a	http://bioguide.congress.gov/bioguide/photo/P/P000593.jpg	\N
183	John	Larson	CT	1	CT01	D	h	\N	\N	\N	1501 Cannon House Office Building Washington DC, 20515	(202) 225-2265	L000557	a	http://bioguide.congress.gov/bioguide/photo/L/L000557.jpg	\N
184	Joe	Courtney	CT	2	CT02	D	h	\N	\N	\N	2348 Rayburn House Office Building Washington DC, 20515	(202) 225-2076	C001069	a	http://bioguide.congress.gov/bioguide/photo/C/C001069.jpg	\N
185	Rosa	DeLauro	CT	3	CT03	D	h	\N	\N	\N	2413 Rayburn House Office Building Washington DC, 20515	(202) 225-3661	D000216	a	http://bioguide.congress.gov/bioguide/photo/D/D000216.jpg	\N
186	James	Himes	CT	4	CT04	D	h	\N	\N	\N	1227 Cannon House Office Building Washington DC, 20515	(202) 225-5541	H001047	a	http://bioguide.congress.gov/bioguide/photo/H/H001047.jpg	\N
187	Elizabeth	Esty	CT	5	CT05	D	h	\N	\N	\N	405 Longworth House Office Building Washington DC, 20515	(202) 225-4476	E000293	a	http://bioguide.congress.gov/bioguide/photo/E/E000293.jpg	\N
188	Eleanor	Norton	DC	0	DC00	D	h	\N	\N	\N	2136 Rayburn House Office Building Washington DC, 20515	(202) 225-8050	N000147	a	http://bioguide.congress.gov/bioguide/photo/N/N000147.jpg	\N
192	Ted	Yoho	FL	3	FL03	R	h	\N	\N	\N	511 Longworth House Office Building Washington DC, 20515	(202) 225-5744	Y000065	a	http://bioguide.congress.gov/bioguide/photo/Y/Y000065.jpg	\N
196	John	Mica	FL	7	FL07	R	h	\N	\N	\N	2187 Rayburn House Office Building Washington DC, 20515	(202) 225-4035	M000689	d	http://bioguide.congress.gov/bioguide/photo/M/M000689.jpg	\N
197	Bill	Posey	FL	8	FL08	R	h	\N	\N	\N	120 Longworth House Office Building Washington DC, 20515	(202) 225-3671	P000599	a	http://bioguide.congress.gov/bioguide/photo/P/P000599.jpg	\N
201	Gus	Bilirakis	FL	12	FL12	R	h	\N	\N	\N	2112 Rayburn House Office Building Washington DC, 20515	(202) 225-5755	B001257	a	http://bioguide.congress.gov/bioguide/photo/B/B001257.jpg	\N
200	Richard	Nugent	FL	11	FL11	R	h	\N	\N	\N	1727 Cannon House Office Building Washington DC, 20515	(202) 225-1002	N000185	r	http://bioguide.congress.gov/bioguide/photo/N/N000185.jpg	Announced retirement on Nov. 2, 2015
199	Daniel	Webster	FL	10	FL10	R	h	\N	\N	\N	1039 Cannon House Office Building Washington DC, 20515	(202) 225-2176	W000806	a	http://bioguide.congress.gov/bioguide/photo/W/W000806.jpg	\N
203	Kathy	Castor	FL	14	FL14	D	h	\N	\N	\N	205 Longworth House Office Building Washington DC, 20515	(202) 225-3376	C001066	a	http://bioguide.congress.gov/bioguide/photo/C/C001066.jpg	\N
204	Dennis	Ross	FL	15	FL15	R	h	\N	\N	\N	229 Longworth House Office Building Washington DC, 20515	(202) 225-1252	R000593	a	http://bioguide.congress.gov/bioguide/photo/R/R000593.jpg	\N
205	Vern	Buchanan	FL	16	FL16	R	h	\N	\N	\N	2104 Rayburn House Office Building Washington DC, 20515	(202) 225-5015	B001260	a	http://bioguide.congress.gov/bioguide/photo/B/B001260.jpg	\N
206	Thomas	Rooney	FL	17	FL17	R	h	\N	\N	\N	2160 Rayburn House Office Building Washington DC, 20515	(202) 225-5792	R000583	a	http://bioguide.congress.gov/bioguide/photo/R/R000583.jpg	\N
209	Alcee	Hastings	FL	20	FL20	D	h	\N	\N	\N	2353 Rayburn House Office Building Washington DC, 20515	(202) 225-1313	H000324	a	http://bioguide.congress.gov/bioguide/photo/H/H000324.jpg	\N
210	Theodore	Deutch	FL	21	FL21	D	h	\N	\N	\N	2447 Rayburn House Office Building Washington DC, 20515	(202) 225-3001	D000610	a	http://bioguide.congress.gov/bioguide/photo/D/D000610.jpg	\N
211	Lois	Frankel	FL	22	FL22	D	h	\N	\N	\N	1037 Cannon House Office Building Washington DC, 20515	(202) 225-9890	F000462	a	http://bioguide.congress.gov/bioguide/photo/F/F000462.jpg	\N
212	Debbie	Wasserman Schultz	FL	23	FL23	D	h	\N	\N	\N	1114 Cannon House Office Building Washington DC, 20515	(202) 225-7931	W000797	a	http://bioguide.congress.gov/bioguide/photo/W/W000797.jpg	\N
213	Frederica	Wilson	FL	24	FL24	D	h	\N	\N	\N	208 Longworth House Office Building Washington DC, 20515	(202) 225-4506	W000808	a	http://bioguide.congress.gov/bioguide/photo/W/W000808.jpg	\N
214	Mario	Diaz-Balart	FL	25	FL25	R	h	\N	\N	\N	440 Longworth House Office Building Washington DC, 20515	(202) 225-4211	D000600	a	http://bioguide.congress.gov/bioguide/photo/D/D000600.jpg	\N
216	Ileana	Ros-Lehtinen	FL	27	FL27	R	h	\N	\N	\N	2206 Rayburn House Office Building Washington DC, 20515	(202) 225-3931	R000435	a	http://bioguide.congress.gov/bioguide/photo/R/R000435.jpg	\N
218	Sanford	Bishop	GA	2	GA02	D	h	\N	\N	\N	2407 Rayburn House Office Building Washington DC, 20515	(202) 225-3631	B000490	a	http://bioguide.congress.gov/bioguide/photo/B/B000490.jpg	\N
220	Henry	Johnson	GA	4	GA04	D	h	\N	\N	\N	2240 Rayburn House Office Building Washington DC, 20515	(202) 225-1605	J000288	a	http://bioguide.congress.gov/bioguide/photo/J/J000288.jpg	\N
221	John	Lewis	GA	5	GA05	D	h	\N	\N	\N	343 Longworth House Office Building Washington DC, 20515	(202) 225-3801	L000287	a	http://bioguide.congress.gov/bioguide/photo/L/L000287.jpg	\N
222	Tom	Price	GA	6	GA06	R	h	\N	\N	\N	100 Longworth House Office Building Washington DC, 20515	(202) 225-4501	P000591	a	http://bioguide.congress.gov/bioguide/photo/P/P000591.jpg	\N
223	Rob	Woodall	GA	7	GA07	R	h	\N	\N	\N	1724 Cannon House Office Building Washington DC, 20515	(202) 225-4272	W000810	a	http://bioguide.congress.gov/bioguide/photo/W/W000810.jpg	\N
224	Austin	Scott	GA	8	GA08	R	h	\N	\N	\N	2417 Rayburn House Office Building Washington DC, 20515	(202) 225-6531	S001189	a	http://bioguide.congress.gov/bioguide/photo/S/S001189.jpg	\N
225	Doug	Collins	GA	9	GA09	R	h	\N	\N	\N	1504 Cannon House Office Building Washington DC, 20515	(202) 225-9893	C001093	a	http://bioguide.congress.gov/bioguide/photo/C/C001093.jpg	\N
226	Jody	Hice	GA	10	GA10	R	h	\N	\N	\N	1516 Cannon House Office Building Washington DC, 20515	(202) 225-4101	H001071	a	http://bioguide.congress.gov/bioguide/photo/H/H001071.jpg	\N
228	Rick	Allen	GA	12	GA12	R	h	\N	\N	\N	513 Longworth House Office Building Washington DC, 20515	(202) 225-2823	A000372	a	http://bioguide.congress.gov/bioguide/photo/A/A000372.jpg	\N
229	David	Scott	GA	13	GA13	D	h	\N	\N	\N	225 Longworth House Office Building Washington DC, 20515	(202) 225-2939	S001157	a	http://bioguide.congress.gov/bioguide/photo/S/S001157.jpg	\N
230	Tom	Graves	GA	14	GA14	R	h	\N	\N	\N	2442 Rayburn House Office Building Washington DC, 20515	(202) 225-5211	G000560	a	http://bioguide.congress.gov/bioguide/photo/G/G000560.jpg	\N
231	Madeleine	Bordallo	GU	0	GU00	D	h	\N	\N	\N	2441 Rayburn House Office Building Washington DC, 20515	(202) 225-1188	B001245	a	http://bioguide.congress.gov/bioguide/photo/B/B001245.jpg	\N
233	Tulsi	Gabbard	HI	2	HI02	D	h	\N	\N	\N	1609 Cannon House Office Building Washington DC, 20515	(202) 225-4906	G000571	a	http://bioguide.congress.gov/bioguide/photo/G/G000571.jpg	\N
235	David	Loebsack	IA	2	IA02	D	h	\N	\N	\N	1527 Cannon House Office Building Washington DC, 20515	(202) 225-6576	L000565	a	http://bioguide.congress.gov/bioguide/photo/L/L000565.jpg	\N
237	Steve	King	IA	4	IA04	R	h	\N	\N	\N	2210 Rayburn House Office Building Washington DC, 20515	(202) 225-4426	K000362	a	http://bioguide.congress.gov/bioguide/photo/K/K000362.jpg	\N
238	Raúl	Labrador	ID	1	ID01	R	h	\N	\N	\N	1523 Cannon House Office Building Washington DC, 20515	(202) 225-6611	L000573	a	http://bioguide.congress.gov/bioguide/photo/L/L000573.jpg	\N
239	Michael	Simpson	ID	2	ID02	R	h	\N	\N	\N	2312 Rayburn House Office Building Washington DC, 20515	(202) 225-5531	S001148	a	http://bioguide.congress.gov/bioguide/photo/S/S001148.jpg	\N
240	Bobby	Rush	IL	1	IL01	D	h	\N	\N	\N	2188 Rayburn House Office Building Washington DC, 20515	(202) 225-4372	R000515	a	http://bioguide.congress.gov/bioguide/photo/R/R000515.jpg	\N
241	Robin	Kelly	IL	2	IL02	D	h	\N	\N	\N	1239 Cannon House Office Building Washington DC, 20515	(202) 225-0773	K000385	a	http://bioguide.congress.gov/bioguide/photo/K/K000385.jpg	\N
242	Daniel	Lipinski	IL	3	IL03	D	h	\N	\N	\N	2346 Rayburn House Office Building Washington DC, 20515	(202) 225-5701	L000563	a	http://bioguide.congress.gov/bioguide/photo/L/L000563.jpg	\N
243	Luis	Gutiérrez	IL	4	IL04	D	h	\N	\N	\N	2408 Rayburn House Office Building Washington DC, 20515	(202) 225-8203	G000535	a	http://bioguide.congress.gov/bioguide/photo/G/G000535.jpg	\N
244	Mike	Quigley	IL	5	IL05	D	h	\N	\N	\N	2458 Rayburn House Office Building Washington DC, 20515	(202) 225-4061	Q000023	a	http://bioguide.congress.gov/bioguide/photo/Q/Q000023.jpg	\N
245	Peter	Roskam	IL	6	IL06	R	h	\N	\N	\N	2246 Rayburn House Office Building Washington DC, 20515	(202) 225-4561	R000580	a	http://bioguide.congress.gov/bioguide/photo/R/R000580.jpg	\N
247	Tammy	Duckworth	IL	8	IL08	D	h	\N	\N	\N	104 Longworth House Office Building Washington DC, 20515	(202) 225-3711	D000622	o	http://bioguide.congress.gov/bioguide/photo/D/D000622.jpg	Running for Senate
246	Danny	Davis	IL	7	IL07	D	h	\N	\N	\N	2159 Rayburn House Office Building Washington DC, 20515	(202) 225-5006	D000096	a	http://bioguide.congress.gov/bioguide/photo/D/D000096.jpg	\N
248	Janice	Schakowsky	IL	9	IL09	D	h	\N	\N	\N	2367 Rayburn House Office Building Washington DC, 20515	(202) 225-2111	S001145	a	http://bioguide.congress.gov/bioguide/photo/S/S001145.jpg	\N
249	Robert	Dold	IL	10	IL10	R	h	\N	\N	\N	221 Longworth House Office Building Washington DC, 20515	(202) 225-4835	D000613	d	http://bioguide.congress.gov/bioguide/photo/D/D000613.jpg	\N
250	Bill	Foster	IL	11	IL11	D	h	\N	\N	\N	1224 Cannon House Office Building Washington DC, 20515	(202) 225-3515	F000454	a	http://bioguide.congress.gov/bioguide/photo/F/F000454.jpg	\N
252	Rodney	Davis	IL	13	IL13	R	h	\N	\N	\N	1740 Cannon House Office Building Washington DC, 20515	(202) 225-2371	D000619	a	http://bioguide.congress.gov/bioguide/photo/D/D000619.jpg	\N
253	Randy	Hultgren	IL	14	IL14	R	h	\N	\N	\N	2455 Rayburn House Office Building Washington DC, 20515	(202) 225-2976	H001059	a	http://bioguide.congress.gov/bioguide/photo/H/H001059.jpg	\N
254	John	Shimkus	IL	15	IL15	R	h	\N	\N	\N	2217 Rayburn House Office Building Washington DC, 20515	(202) 225-5271	S000364	a	http://bioguide.congress.gov/bioguide/photo/S/S000364.jpg	\N
255	Adam	Kinzinger	IL	16	IL16	R	h	\N	\N	\N	1221 Cannon House Office Building Washington DC, 20515	(202) 225-3635	K000378	a	http://bioguide.congress.gov/bioguide/photo/K/K000378.jpg	\N
256	Cheri	Bustos	IL	17	IL17	D	h	\N	\N	\N	1009 Cannon House Office Building Washington DC, 20515	(202) 225-5905	B001286	a	http://bioguide.congress.gov/bioguide/photo/B/B001286.jpg	\N
258	Peter	Visclosky	IN	1	IN01	D	h	\N	\N	\N	2328 Rayburn House Office Building Washington DC, 20515	(202) 225-2461	V000108	a	http://bioguide.congress.gov/bioguide/photo/V/V000108.jpg	\N
259	Jackie	Walorski	IN	2	IN02	R	h	\N	\N	\N	419 Longworth House Office Building Washington DC, 20515	(202) 225-3915	W000813	a	http://bioguide.congress.gov/bioguide/photo/W/W000813.jpg	\N
262	Susan	Brooks	IN	5	IN05	R	h	\N	\N	\N	1505 Cannon House Office Building Washington DC, 20515	(202) 225-2276	B001284	a	http://bioguide.congress.gov/bioguide/photo/B/B001284.jpg	\N
263	Luke	Messer	IN	6	IN06	R	h	\N	\N	\N	508 Longworth House Office Building Washington DC, 20515	(202) 225-3021	M001189	a	http://bioguide.congress.gov/bioguide/photo/M/M001189.jpg	\N
264	André	Carson	IN	7	IN07	D	h	\N	\N	\N	2453 Rayburn House Office Building Washington DC, 20515	(202) 225-4011	C001072	a	http://bioguide.congress.gov/bioguide/photo/C/C001072.jpg	\N
268	Lynn	Jenkins	KS	2	KS02	R	h	\N	\N	\N	1526 Cannon House Office Building Washington DC, 20515	(202) 225-6601	J000290	a	http://bioguide.congress.gov/bioguide/photo/J/J000290.jpg	\N
270	Mike	Pompeo	KS	4	KS04	R	h	\N	\N	\N	436 Longworth House Office Building Washington DC, 20515	(202) 225-6216	P000602	a	http://bioguide.congress.gov/bioguide/photo/P/P000602.jpg	\N
272	Brett	Guthrie	KY	2	KY02	R	h	\N	\N	\N	2434 Rayburn House Office Building Washington DC, 20515	(202) 225-3501	G000558	a	http://bioguide.congress.gov/bioguide/photo/G/G000558.jpg	\N
273	John	Yarmuth	KY	3	KY03	D	h	\N	\N	\N	403 Longworth House Office Building Washington DC, 20515	(202) 225-5401	Y000062	a	http://bioguide.congress.gov/bioguide/photo/Y/Y000062.jpg	\N
274	Thomas	Massie	KY	4	KY04	R	h	\N	\N	\N	314 Longworth House Office Building Washington DC, 20515	(202) 225-3465	M001184	a	http://bioguide.congress.gov/bioguide/photo/M/M001184.jpg	\N
275	Harold	Rogers	KY	5	KY05	R	h	\N	\N	\N	2406 Rayburn House Office Building Washington DC, 20515	(202) 225-4601	R000395	a	http://bioguide.congress.gov/bioguide/photo/R/R000395.jpg	\N
276	Andy	Barr	KY	6	KY06	R	h	\N	\N	\N	1432 Cannon House Office Building Washington DC, 20515	(202) 225-4706	B001282	a	http://bioguide.congress.gov/bioguide/photo/B/B001282.jpg	\N
277	Steve	Scalise	LA	1	LA01	R	h	\N	\N	\N	2338 Rayburn House Office Building Washington DC, 20515	(202) 225-3015	S001176	a	http://bioguide.congress.gov/bioguide/photo/S/S001176.jpg	\N
278	Cedric	Richmond	LA	2	LA02	D	h	\N	\N	\N	240 Longworth House Office Building Washington DC, 20515	(202) 225-6636	R000588	a	http://bioguide.congress.gov/bioguide/photo/R/R000588.jpg	\N
281	Ralph	Abraham	LA	5	LA05	R	h	\N	\N	\N	417 Longworth House Office Building Washington DC, 20515	(202) 225-8490	A000374	a	http://bioguide.congress.gov/bioguide/photo/A/A000374.jpg	\N
283	Richard	Neal	MA	1	MA01	D	h	\N	\N	\N	341 Longworth House Office Building Washington DC, 20515	(202) 225-5601	N000015	a	http://bioguide.congress.gov/bioguide/photo/N/N000015.jpg	\N
284	James	McGovern	MA	2	MA02	D	h	\N	\N	\N	438 Longworth House Office Building Washington DC, 20515	(202) 225-6101	M000312	a	http://bioguide.congress.gov/bioguide/photo/M/M000312.jpg	\N
285	Niki	Tsongas	MA	3	MA03	D	h	\N	\N	\N	1714 Cannon House Office Building Washington DC, 20515	(202) 225-3411	T000465	a	http://bioguide.congress.gov/bioguide/photo/T/T000465.jpg	\N
332	Gregorio	Sablan	MP	0	MP00	D	h	\N	\N	\N	423 Longworth House Office Building Washington DC, 20515	(202) 225-2646	S001177	a	http://bioguide.congress.gov/bioguide/photo/S/S001177.jpg	\N
286	Joseph	Kennedy	MA	4	MA04	D	h	\N	\N	\N	306 Longworth House Office Building Washington DC, 20515	(202) 225-5931	K000379	a	http://bioguide.congress.gov/bioguide/photo/K/K000379.jpg	\N
287	Katherine	Clark	MA	5	MA05	D	h	\N	\N	\N	1721 Cannon House Office Building Washington DC, 20515	(202) 225-2836	C001101	a	http://bioguide.congress.gov/bioguide/photo/C/C001101.jpg	\N
288	Seth	Moulton	MA	6	MA06	D	h	\N	\N	\N	1408 Cannon House Office Building Washington DC, 20515	(202) 225-8020	M001196	a	http://bioguide.congress.gov/bioguide/photo/M/M001196.jpg	\N
289	Michael	Capuano	MA	7	MA07	D	h	\N	\N	\N	1414 Cannon House Office Building Washington DC, 20515	(202) 225-5111	C001037	a	http://bioguide.congress.gov/bioguide/photo/C/C001037.jpg	\N
290	Stephen	Lynch	MA	8	MA08	D	h	\N	\N	\N	2369 Rayburn House Office Building Washington DC, 20515	(202) 225-8273	L000562	a	http://bioguide.congress.gov/bioguide/photo/L/L000562.jpg	\N
291	William	Keating	MA	9	MA09	D	h	\N	\N	\N	315 Longworth House Office Building Washington DC, 20515	(202) 225-3111	K000375	a	http://bioguide.congress.gov/bioguide/photo/K/K000375.jpg	\N
292	Andy	Harris	MD	1	MD01	R	h	\N	\N	\N	1533 Cannon House Office Building Washington DC, 20515	(202) 225-5311	H001052	a	http://bioguide.congress.gov/bioguide/photo/H/H001052.jpg	\N
293	C.	Ruppersberger	MD	2	MD02	D	h	\N	\N	\N	2416 Rayburn House Office Building Washington DC, 20515	(202) 225-3061	R000576	a	http://bioguide.congress.gov/bioguide/photo/R/R000576.jpg	\N
294	John	Sarbanes	MD	3	MD03	D	h	\N	\N	\N	2444 Rayburn House Office Building Washington DC, 20515	(202) 225-4016	S001168	a	http://bioguide.congress.gov/bioguide/photo/S/S001168.jpg	\N
296	Steny	Hoyer	MD	5	MD05	D	h	\N	\N	\N	1705 Cannon House Office Building Washington DC, 20515	(202) 225-4131	H000874	a	http://bioguide.congress.gov/bioguide/photo/H/H000874.jpg	\N
297	John	Delaney	MD	6	MD06	D	h	\N	\N	\N	1632 Cannon House Office Building Washington DC, 20515	(202) 225-2721	D000620	a	http://bioguide.congress.gov/bioguide/photo/D/D000620.jpg	\N
298	Elijah	Cummings	MD	7	MD07	D	h	\N	\N	\N	2230 Rayburn House Office Building Washington DC, 20515	(202) 225-4741	C000984	a	http://bioguide.congress.gov/bioguide/photo/C/C000984.jpg	\N
300	Chellie	Pingree	ME	1	ME01	D	h	\N	\N	\N	2162 Rayburn House Office Building Washington DC, 20515	(202) 225-6116	P000597	a	http://bioguide.congress.gov/bioguide/photo/P/P000597.jpg	\N
303	Bill	Huizenga	MI	2	MI02	R	h	\N	\N	\N	1217 Cannon House Office Building Washington DC, 20515	(202) 225-4401	H001058	a	http://bioguide.congress.gov/bioguide/photo/H/H001058.jpg	\N
304	Justin	Amash	MI	3	MI03	R	h	\N	\N	\N	114 Longworth House Office Building Washington DC, 20515	(202) 225-3831	A000367	a	http://bioguide.congress.gov/bioguide/photo/A/A000367.jpg	\N
305	John	Moolenaar	MI	4	MI04	R	h	\N	\N	\N	117 Longworth House Office Building Washington DC, 20515	(202) 225-3561	M001194	a	http://bioguide.congress.gov/bioguide/photo/M/M001194.jpg	\N
306	Daniel	Kildee	MI	5	MI05	D	h	\N	\N	\N	227 Longworth House Office Building Washington DC, 20515	(202) 225-3611	K000380	a	http://bioguide.congress.gov/bioguide/photo/K/K000380.jpg	\N
307	Fred	Upton	MI	6	MI06	R	h	\N	\N	\N	2183 Rayburn House Office Building Washington DC, 20515	(202) 225-3761	U000031	a	http://bioguide.congress.gov/bioguide/photo/U/U000031.jpg	\N
308	Tim	Walberg	MI	7	MI07	R	h	\N	\N	\N	2436 Rayburn House Office Building Washington DC, 20515	(202) 225-6276	W000798	a	http://bioguide.congress.gov/bioguide/photo/W/W000798.jpg	\N
310	Sander	Levin	MI	9	MI09	D	h	\N	\N	\N	1236 Cannon House Office Building Washington DC, 20515	(202) 225-4961	L000263	a	http://bioguide.congress.gov/bioguide/photo/L/L000263.jpg	\N
314	John	Conyers	MI	13	MI13	D	h	\N	\N	\N	2426 Rayburn House Office Building Washington DC, 20515	(202) 225-5126	C000714	a	http://bioguide.congress.gov/bioguide/photo/C/C000714.jpg	\N
316	Timothy	Walz	MN	1	MN01	D	h	\N	\N	\N	1034 Cannon House Office Building Washington DC, 20515	(202) 225-2472	W000799	a	http://bioguide.congress.gov/bioguide/photo/W/W000799.jpg	\N
318	Erik	Paulsen	MN	3	MN03	R	h	\N	\N	\N	127 Longworth House Office Building Washington DC, 20515	(202) 225-2871	P000594	a	http://bioguide.congress.gov/bioguide/photo/P/P000594.jpg	\N
319	Betty	McCollum	MN	4	MN04	D	h	\N	\N	\N	2256 Rayburn House Office Building Washington DC, 20515	(202) 225-6631	M001143	a	http://bioguide.congress.gov/bioguide/photo/M/M001143.jpg	\N
320	Keith	Ellison	MN	5	MN05	D	h	\N	\N	\N	2263 Rayburn House Office Building Washington DC, 20515	(202) 225-4755	E000288	a	http://bioguide.congress.gov/bioguide/photo/E/E000288.jpg	\N
322	Collin	Peterson	MN	7	MN07	D	h	\N	\N	\N	2204 Rayburn House Office Building Washington DC, 20515	(202) 225-2165	P000258	a	http://bioguide.congress.gov/bioguide/photo/P/P000258.jpg	\N
323	Richard	Nolan	MN	8	MN08	D	h	\N	\N	\N	2366 Rayburn House Office Building Washington DC, 20515	(202) 225-6211	N000127	a	http://bioguide.congress.gov/bioguide/photo/N/N000127.jpg	\N
324	Wm.	Clay	MO	1	MO01	D	h	\N	\N	\N	2428 Rayburn House Office Building Washington DC, 20515	(202) 225-2406	C001049	a	http://bioguide.congress.gov/bioguide/photo/C/C001049.jpg	\N
325	Ann	Wagner	MO	2	MO02	R	h	\N	\N	\N	435 Longworth House Office Building Washington DC, 20515	(202) 225-1621	W000812	a	http://bioguide.congress.gov/bioguide/photo/W/W000812.jpg	\N
326	Blaine	Luetkemeyer	MO	3	MO03	R	h	\N	\N	\N	2440 Rayburn House Office Building Washington DC, 20515	(202) 225-2956	L000569	a	http://bioguide.congress.gov/bioguide/photo/L/L000569.jpg	\N
327	Vicky	Hartzler	MO	4	MO04	R	h	\N	\N	\N	2235 Rayburn House Office Building Washington DC, 20515	(202) 225-2876	H001053	a	http://bioguide.congress.gov/bioguide/photo/H/H001053.jpg	\N
328	Emanuel	Cleaver	MO	5	MO05	D	h	\N	\N	\N	2335 Rayburn House Office Building Washington DC, 20515	(202) 225-4535	C001061	a	http://bioguide.congress.gov/bioguide/photo/C/C001061.jpg	\N
379	Kathleen	Rice	NY	4	NY04	D	h	\N	\N	\N	1508 Cannon House Office Building Washington DC, 20515	(202) 225-5516	R000602	a	\N	\N
329	Sam	Graves	MO	6	MO06	R	h	\N	\N	\N	1415 Cannon House Office Building Washington DC, 20515	(202) 225-7041	G000546	a	http://bioguide.congress.gov/bioguide/photo/G/G000546.jpg	\N
330	Billy	Long	MO	7	MO07	R	h	\N	\N	\N	1541 Cannon House Office Building Washington DC, 20515	(202) 225-6536	L000576	a	http://bioguide.congress.gov/bioguide/photo/L/L000576.jpg	\N
331	Jason	Smith	MO	8	MO08	R	h	\N	\N	\N	1118 Cannon House Office Building Washington DC, 20515	(202) 225-4404	S001195	a	http://bioguide.congress.gov/bioguide/photo/S/S001195.jpg	\N
334	Bennie	Thompson	MS	2	MS02	D	h	\N	\N	\N	2466 Rayburn House Office Building Washington DC, 20515	(202) 225-5876	T000193	a	http://bioguide.congress.gov/bioguide/photo/T/T000193.jpg	\N
335	Gregg	Harper	MS	3	MS03	R	h	\N	\N	\N	307 Longworth House Office Building Washington DC, 20515	(202) 225-5031	H001045	a	http://bioguide.congress.gov/bioguide/photo/H/H001045.jpg	\N
336	Steven	Palazzo	MS	4	MS04	R	h	\N	\N	\N	331 Longworth House Office Building Washington DC, 20515	(202) 225-5772	P000601	a	http://bioguide.congress.gov/bioguide/photo/P/P000601.jpg	\N
338	G.	Butterfield	NC	1	NC01	D	h	\N	\N	\N	2305 Rayburn House Office Building Washington DC, 20515	(202) 225-3101	B001251	a	http://bioguide.congress.gov/bioguide/photo/B/B001251.jpg	\N
340	Walter	Jones	NC	3	NC03	R	h	\N	\N	\N	2333 Rayburn House Office Building Washington DC, 20515	(202) 225-3415	J000255	a	http://bioguide.congress.gov/bioguide/photo/J/J000255.jpg	\N
341	David	Price	NC	4	NC04	D	h	\N	\N	\N	2108 Rayburn House Office Building Washington DC, 20515	(202) 225-1784	P000523	a	http://bioguide.congress.gov/bioguide/photo/P/P000523.jpg	\N
342	Virginia	Foxx	NC	5	NC05	R	h	\N	\N	\N	2350 Rayburn House Office Building Washington DC, 20515	(202) 225-2071	F000450	a	http://bioguide.congress.gov/bioguide/photo/F/F000450.jpg	\N
345	Richard	Hudson	NC	8	NC08	R	h	\N	\N	\N	429 Longworth House Office Building Washington DC, 20515	(202) 225-3715	H001067	a	http://bioguide.congress.gov/bioguide/photo/H/H001067.jpg	\N
346	Robert	Pittenger	NC	9	NC09	R	h	\N	\N	\N	224 Longworth House Office Building Washington DC, 20515	(202) 225-1976	P000606	a	http://bioguide.congress.gov/bioguide/photo/P/P000606.jpg	\N
347	Patrick	McHenry	NC	10	NC10	R	h	\N	\N	\N	2334 Rayburn House Office Building Washington DC, 20515	(202) 225-2576	M001156	a	http://bioguide.congress.gov/bioguide/photo/M/M001156.jpg	\N
350	George	Holding	NC	13	NC13	R	h	\N	\N	\N	507 Longworth House Office Building Washington DC, 20515	(202) 225-3032	H001065	a	http://bioguide.congress.gov/bioguide/photo/H/H001065.jpg	\N
348	Mark	Meadows	NC	11	NC11	R	h	\N	\N	\N	1024 Cannon House Office Building Washington DC, 20515	(202) 225-6401	M001187	a	http://bioguide.congress.gov/bioguide/photo/M/M001187.jpg	\N
351	Kevin	Cramer	ND	0	ND00	R	h	\N	\N	\N	1032 Cannon House Office Building Washington DC, 20515	(202) 225-2611	C001096	a	http://bioguide.congress.gov/bioguide/photo/C/C001096.jpg	\N
352	Jeff	Fortenberry	NE	1	NE01	R	h	\N	\N	\N	1514 Cannon House Office Building Washington DC, 20515	(202) 225-4806	F000449	a	http://bioguide.congress.gov/bioguide/photo/F/F000449.jpg	\N
353	Brad	Ashford	NE	2	NE02	D	h	\N	\N	\N	107 Longworth House Office Building Washington DC, 20515	(202) 225-4155	A000373	d	http://bioguide.congress.gov/bioguide/photo/A/A000373.jpg	\N
354	Adrian	Smith	NE	3	NE03	R	h	\N	\N	\N	2241 Rayburn House Office Building Washington DC, 20515	(202) 225-6435	S001172	a	http://bioguide.congress.gov/bioguide/photo/S/S001172.jpg	\N
355	Frank	Guinta	NH	1	NH01	R	h	\N	\N	\N	326 Longworth House Office Building Washington DC, 20515	(202) 225-5456	G000570	d	http://bioguide.congress.gov/bioguide/photo/G/G000570.jpg	\N
356	Ann	Kuster	NH	2	NH02	D	h	\N	\N	\N	137 Longworth House Office Building Washington DC, 20515	(202) 225-5206	K000382	a	http://bioguide.congress.gov/bioguide/photo/K/K000382.jpg	\N
357	Donald	Norcross	NJ	1	NJ01	D	h	\N	\N	\N	1531 Cannon House Office Building Washington DC, 20515	(202) 225-6501	N000188	a	http://bioguide.congress.gov/bioguide/photo/N/N000188.jpg	\N
358	Frank	LoBiondo	NJ	2	NJ02	R	h	\N	\N	\N	2427 Rayburn House Office Building Washington DC, 20515	(202) 225-6572	L000554	a	http://bioguide.congress.gov/bioguide/photo/L/L000554.jpg	\N
359	Thomas	MacArthur	NJ	3	NJ03	R	h	\N	\N	\N	506 Longworth House Office Building Washington DC, 20515	(202) 225-4765	M001193	a	http://bioguide.congress.gov/bioguide/photo/M/M001193.jpg	\N
360	Christopher	Smith	NJ	4	NJ04	R	h	\N	\N	\N	2373 Rayburn House Office Building Washington DC, 20515	(202) 225-3765	S000522	a	http://bioguide.congress.gov/bioguide/photo/S/S000522.jpg	\N
361	Scott	Garrett	NJ	5	NJ05	R	h	\N	\N	\N	2232 Rayburn House Office Building Washington DC, 20515	(202) 225-4465	G000548	d	http://bioguide.congress.gov/bioguide/photo/G/G000548.jpg	\N
362	Frank	Pallone	NJ	6	NJ06	D	h	\N	\N	\N	237 Longworth House Office Building Washington DC, 20515	(202) 225-4671	P000034	a	http://bioguide.congress.gov/bioguide/photo/P/P000034.jpg	\N
363	Leonard	Lance	NJ	7	NJ07	R	h	\N	\N	\N	2352 Rayburn House Office Building Washington DC, 20515	(202) 225-5361	L000567	a	http://bioguide.congress.gov/bioguide/photo/L/L000567.jpg	\N
364	Albio	Sires	NJ	8	NJ08	D	h	\N	\N	\N	2342 Rayburn House Office Building Washington DC, 20515	(202) 225-7919	S001165	a	http://bioguide.congress.gov/bioguide/photo/S/S001165.jpg	\N
365	Bill	Pascrell	NJ	9	NJ09	D	h	\N	\N	\N	2370 Rayburn House Office Building Washington DC, 20515	(202) 225-5751	P000096	a	http://bioguide.congress.gov/bioguide/photo/P/P000096.jpg	\N
366	Donald	Payne	NJ	10	NJ10	D	h	\N	\N	\N	103 Longworth House Office Building Washington DC, 20515	(202) 225-3436	P000604	a	http://bioguide.congress.gov/bioguide/photo/P/P000604.jpg	\N
367	Rodney	Frelinghuysen	NJ	11	NJ11	R	h	\N	\N	\N	2306 Rayburn House Office Building Washington DC, 20515	(202) 225-5034	F000372	a	http://bioguide.congress.gov/bioguide/photo/F/F000372.jpg	\N
368	Bonnie	Watson Coleman	NJ	12	NJ12	D	h	\N	\N	\N	126 Longworth House Office Building Washington DC, 20515	(202) 225-5801	W000822	a	http://bioguide.congress.gov/bioguide/photo/W/W000822.jpg	\N
369	Michelle	Lujan Grisham	NM	1	NM01	D	h	\N	\N	\N	214 Longworth House Office Building Washington DC, 20515	(202) 225-6316	L000580	a	http://bioguide.congress.gov/bioguide/photo/L/L000580.jpg	\N
370	Stevan	Pearce	NM	2	NM02	R	h	\N	\N	\N	2432 Rayburn House Office Building Washington DC, 20515	(202) 225-2365	P000588	a	http://bioguide.congress.gov/bioguide/photo/P/P000588.jpg	\N
518	Stacey	Plaskett	VI	0	VI00	D	h	\N	\N	\N	509 Longworth House Office Building Washington DC, 20515	(202) 225-1790	P000610	a	\N	\N
371	Ben	Luján	NM	3	NM03	D	h	\N	\N	\N	2446 Rayburn House Office Building Washington DC, 20515	(202) 225-6190	L000570	a	http://bioguide.congress.gov/bioguide/photo/L/L000570.jpg	\N
372	Dina	Titus	NV	1	NV01	D	h	\N	\N	\N	401 Longworth House Office Building Washington DC, 20515	(202) 225-5965	T000468	a	http://bioguide.congress.gov/bioguide/photo/T/T000468.jpg	\N
373	Mark	Amodei	NV	2	NV02	R	h	\N	\N	\N	332 Longworth House Office Building Washington DC, 20515	(202) 225-6155	A000369	a	http://bioguide.congress.gov/bioguide/photo/A/A000369.jpg	\N
377	Peter	King	NY	2	NY02	R	h	\N	\N	\N	339 Longworth House Office Building Washington DC, 20515	(202) 225-7896	K000210	a	http://bioguide.congress.gov/bioguide/photo/K/K000210.jpg	\N
380	Gregory	Meeks	NY	5	NY05	D	h	\N	\N	\N	2234 Rayburn House Office Building Washington DC, 20515	(202) 225-3461	M001137	a	http://bioguide.congress.gov/bioguide/photo/M/M001137.jpg	\N
381	Grace	Meng	NY	6	NY06	D	h	\N	\N	\N	1317 Cannon House Office Building Washington DC, 20515	(202) 225-2601	M001188	a	http://bioguide.congress.gov/bioguide/photo/M/M001188.jpg	\N
382	Nydia	Velázquez	NY	7	NY07	D	h	\N	\N	\N	2302 Rayburn House Office Building Washington DC, 20515	(202) 225-2361	V000081	a	http://bioguide.congress.gov/bioguide/photo/V/V000081.jpg	\N
383	Hakeem	Jeffries	NY	8	NY08	D	h	\N	\N	\N	1607 Cannon House Office Building Washington DC, 20515	(202) 225-5936	J000294	a	http://bioguide.congress.gov/bioguide/photo/J/J000294.jpg	\N
384	Yvette	Clarke	NY	9	NY09	D	h	\N	\N	\N	2351 Rayburn House Office Building Washington DC, 20515	(202) 225-6231	C001067	a	http://bioguide.congress.gov/bioguide/photo/C/C001067.jpg	\N
385	Jerrold	Nadler	NY	10	NY10	D	h	\N	\N	\N	2109 Rayburn House Office Building Washington DC, 20515	(202) 225-5635	N000002	a	http://bioguide.congress.gov/bioguide/photo/N/N000002.jpg	\N
387	Carolyn	Maloney	NY	12	NY12	D	h	\N	\N	\N	2308 Rayburn House Office Building Washington DC, 20515	(202) 225-7944	M000087	a	http://bioguide.congress.gov/bioguide/photo/M/M000087.jpg	\N
389	Joseph	Crowley	NY	14	NY14	D	h	\N	\N	\N	1436 Cannon House Office Building Washington DC, 20515	(202) 225-3965	C001038	a	http://bioguide.congress.gov/bioguide/photo/C/C001038.jpg	\N
390	José	Serrano	NY	15	NY15	D	h	\N	\N	\N	2227 Rayburn House Office Building Washington DC, 20515	(202) 225-4361	S000248	a	http://bioguide.congress.gov/bioguide/photo/S/S000248.jpg	\N
391	Eliot	Engel	NY	16	NY16	D	h	\N	\N	\N	2462 Rayburn House Office Building Washington DC, 20515	(202) 225-2464	E000179	a	http://bioguide.congress.gov/bioguide/photo/E/E000179.jpg	\N
392	Nita	Lowey	NY	17	NY17	D	h	\N	\N	\N	2365 Rayburn House Office Building Washington DC, 20515	(202) 225-6506	L000480	a	http://bioguide.congress.gov/bioguide/photo/L/L000480.jpg	\N
393	Sean	Maloney	NY	18	NY18	D	h	\N	\N	\N	1529 Cannon House Office Building Washington DC, 20515	(202) 225-5441	M001185	a	http://bioguide.congress.gov/bioguide/photo/M/M001185.jpg	\N
395	Paul	Tonko	NY	20	NY20	D	h	\N	\N	\N	2463 Rayburn House Office Building Washington DC, 20515	(202) 225-5076	T000469	a	http://bioguide.congress.gov/bioguide/photo/T/T000469.jpg	\N
398	Tom	Reed	NY	23	NY23	R	h	\N	\N	\N	2437 Rayburn House Office Building Washington DC, 20515	(202) 225-3161	R000585	a	http://bioguide.congress.gov/bioguide/photo/R/R000585.jpg	\N
400	Louise	Slaughter	NY	25	NY25	D	h	\N	\N	\N	2469 Rayburn House Office Building Washington DC, 20515	(202) 225-3615	S000480	a	http://bioguide.congress.gov/bioguide/photo/S/S000480.jpg	\N
401	Brian	Higgins	NY	26	NY26	D	h	\N	\N	\N	2459 Rayburn House Office Building Washington DC, 20515	(202) 225-3306	H001038	a	http://bioguide.congress.gov/bioguide/photo/H/H001038.jpg	\N
402	Chris	Collins	NY	27	NY27	R	h	\N	\N	\N	1117 Cannon House Office Building Washington DC, 20515	(202) 225-5265	C001092	a	http://bioguide.congress.gov/bioguide/photo/C/C001092.jpg	\N
403	Steve	Chabot	OH	1	OH01	R	h	\N	\N	\N	2371 Rayburn House Office Building Washington DC, 20515	(202) 225-2216	C000266	a	http://bioguide.congress.gov/bioguide/photo/C/C000266.jpg	\N
404	Brad	Wenstrup	OH	2	OH02	R	h	\N	\N	\N	1318 Cannon House Office Building Washington DC, 20515	(202) 225-3164	W000815	a	http://bioguide.congress.gov/bioguide/photo/W/W000815.jpg	\N
405	Joyce	Beatty	OH	3	OH03	D	h	\N	\N	\N	133 Longworth House Office Building Washington DC, 20515	(202) 225-4324	B001281	a	http://bioguide.congress.gov/bioguide/photo/B/B001281.jpg	\N
406	Jim	Jordan	OH	4	OH04	R	h	\N	\N	\N	1524 Cannon House Office Building Washington DC, 20515	(202) 225-2676	J000289	a	http://bioguide.congress.gov/bioguide/photo/J/J000289.jpg	\N
407	Robert	Latta	OH	5	OH05	R	h	\N	\N	\N	2448 Rayburn House Office Building Washington DC, 20515	(202) 225-6405	L000566	a	http://bioguide.congress.gov/bioguide/photo/L/L000566.jpg	\N
408	Bill	Johnson	OH	6	OH06	R	h	\N	\N	\N	1710 Cannon House Office Building Washington DC, 20515	(202) 225-5705	J000292	a	http://bioguide.congress.gov/bioguide/photo/J/J000292.jpg	\N
374	Joseph	Heck	NV	3	NV03	R	h	\N	\N	\N	132 Longworth House Office Building Washington DC, 20515	(202) 225-3252	H001055	o	http://bioguide.congress.gov/bioguide/photo/H/H001055.jpg	Running for Senate
409	Bob	Gibbs	OH	7	OH07	R	h	\N	\N	\N	329 Longworth House Office Building Washington DC, 20515	(202) 225-6265	G000563	a	http://bioguide.congress.gov/bioguide/photo/G/G000563.jpg	\N
411	Marcy	Kaptur	OH	9	OH09	D	h	\N	\N	\N	2186 Rayburn House Office Building Washington DC, 20515	(202) 225-4146	K000009	a	http://bioguide.congress.gov/bioguide/photo/K/K000009.jpg	\N
412	Michael	Turner	OH	10	OH10	R	h	\N	\N	\N	2239 Rayburn House Office Building Washington DC, 20515	(202) 225-6465	T000463	a	http://bioguide.congress.gov/bioguide/photo/T/T000463.jpg	\N
413	Marcia	Fudge	OH	11	OH11	D	h	\N	\N	\N	2344 Rayburn House Office Building Washington DC, 20515	(202) 225-7032	F000455	a	http://bioguide.congress.gov/bioguide/photo/F/F000455.jpg	\N
414	Patrick	Tiberi	OH	12	OH12	R	h	\N	\N	\N	1203 Cannon House Office Building Washington DC, 20515	(202) 225-5355	T000462	a	http://bioguide.congress.gov/bioguide/photo/T/T000462.jpg	\N
415	Tim	Ryan	OH	13	OH13	D	h	\N	\N	\N	1421 Cannon House Office Building Washington DC, 20515	(202) 225-5261	R000577	a	http://bioguide.congress.gov/bioguide/photo/R/R000577.jpg	\N
416	David	Joyce	OH	14	OH14	R	h	\N	\N	\N	1124 Cannon House Office Building Washington DC, 20515	(202) 225-5731	J000295	a	http://bioguide.congress.gov/bioguide/photo/J/J000295.jpg	\N
418	James	Renacci	OH	16	OH16	R	h	\N	\N	\N	328 Longworth House Office Building Washington DC, 20515	(202) 225-3876	R000586	a	http://bioguide.congress.gov/bioguide/photo/R/R000586.jpg	\N
436	Michael	Fitzpatrick	PA	8	PA08	R	h	\N	\N	\N	2400 Rayburn House Office Building Washington DC, 20515	(202) 225-4276	F000451	r	http://bioguide.congress.gov/bioguide/photo/F/F000451.jpg	Announced retirement on Nov. 10, 2014
444	Joseph	Pitts	PA	16	PA16	R	h	\N	\N	\N	420 Longworth House Office Building Washington DC, 20515	(202) 225-2411	P000373	r	http://bioguide.congress.gov/bioguide/photo/P/P000373.jpg	Announced retirement on Nov. 6, 2015
540	Evan	Jenkins	WV	3	WV03	R	h	\N	\N	\N	502 Longworth House Office Building Washington DC, 20515	(202) 225-3452	J000297	a	\N	\N
419	Jim	Bridenstine	OK	1	OK01	R	h	\N	\N	\N	216 Longworth House Office Building Washington DC, 20515	(202) 225-2211	B001283	a	http://bioguide.congress.gov/bioguide/photo/B/B001283.jpg	\N
420	Markwayne	Mullin	OK	2	OK02	R	h	\N	\N	\N	1113 Cannon House Office Building Washington DC, 20515	(202) 225-2701	M001190	a	http://bioguide.congress.gov/bioguide/photo/M/M001190.jpg	\N
421	Frank	Lucas	OK	3	OK03	R	h	\N	\N	\N	2405 Rayburn House Office Building Washington DC, 20515	(202) 225-5565	L000491	a	http://bioguide.congress.gov/bioguide/photo/L/L000491.jpg	\N
422	Tom	Cole	OK	4	OK04	R	h	\N	\N	\N	2467 Rayburn House Office Building Washington DC, 20515	(202) 225-6165	C001053	a	http://bioguide.congress.gov/bioguide/photo/C/C001053.jpg	\N
423	Steve	Russell	OK	5	OK05	R	h	\N	\N	\N	128 Longworth House Office Building Washington DC, 20515	(202) 225-2132	R000604	a	http://bioguide.congress.gov/bioguide/photo/R/R000604.jpg	\N
425	Greg	Walden	OR	2	OR02	R	h	\N	\N	\N	2185 Rayburn House Office Building Washington DC, 20515	(202) 225-6730	W000791	a	http://bioguide.congress.gov/bioguide/photo/W/W000791.jpg	\N
426	Earl	Blumenauer	OR	3	OR03	D	h	\N	\N	\N	1111 Cannon House Office Building Washington DC, 20515	(202) 225-4811	B000574	a	http://bioguide.congress.gov/bioguide/photo/B/B000574.jpg	\N
427	Peter	DeFazio	OR	4	OR04	D	h	\N	\N	\N	2134 Rayburn House Office Building Washington DC, 20515	(202) 225-6416	D000191	a	http://bioguide.congress.gov/bioguide/photo/D/D000191.jpg	\N
428	Kurt	Schrader	OR	5	OR05	D	h	\N	\N	\N	2431 Rayburn House Office Building Washington DC, 20515	(202) 225-5711	S001180	a	http://bioguide.congress.gov/bioguide/photo/S/S001180.jpg	\N
429	Robert	Brady	PA	1	PA01	D	h	\N	\N	\N	102 Longworth House Office Building Washington DC, 20515	(202) 225-4731	B001227	a	http://bioguide.congress.gov/bioguide/photo/B/B001227.jpg	\N
431	Mike	Kelly	PA	3	PA03	R	h	\N	\N	\N	1519 Cannon House Office Building Washington DC, 20515	(202) 225-5406	K000376	a	http://bioguide.congress.gov/bioguide/photo/K/K000376.jpg	\N
432	Scott	Perry	PA	4	PA04	R	h	\N	\N	\N	1207 Cannon House Office Building Washington DC, 20515	(202) 225-5836	P000605	a	http://bioguide.congress.gov/bioguide/photo/P/P000605.jpg	\N
433	Glenn	Thompson	PA	5	PA05	R	h	\N	\N	\N	124 Longworth House Office Building Washington DC, 20515	(202) 225-5121	T000467	a	http://bioguide.congress.gov/bioguide/photo/T/T000467.jpg	\N
435	Patrick	Meehan	PA	7	PA07	R	h	\N	\N	\N	434 Longworth House Office Building Washington DC, 20515	(202) 225-2011	M001181	a	http://bioguide.congress.gov/bioguide/photo/M/M001181.jpg	\N
437	Bill	Shuster	PA	9	PA09	R	h	\N	\N	\N	2268 Rayburn House Office Building Washington DC, 20515	(202) 225-2431	S001154	a	http://bioguide.congress.gov/bioguide/photo/S/S001154.jpg	\N
438	Tom	Marino	PA	10	PA10	R	h	\N	\N	\N	410 Longworth House Office Building Washington DC, 20515	(202) 225-3731	M001179	a	http://bioguide.congress.gov/bioguide/photo/M/M001179.jpg	\N
439	Lou	Barletta	PA	11	PA11	R	h	\N	\N	\N	115 Longworth House Office Building Washington DC, 20515	(202) 225-6511	B001269	a	http://bioguide.congress.gov/bioguide/photo/B/B001269.jpg	\N
440	Keith	Rothfus	PA	12	PA12	R	h	\N	\N	\N	1205 Cannon House Office Building Washington DC, 20515	(202) 225-2065	R000598	a	http://bioguide.congress.gov/bioguide/photo/R/R000598.jpg	\N
442	Michael	Doyle	PA	14	PA14	D	h	\N	\N	\N	239 Longworth House Office Building Washington DC, 20515	(202) 225-2135	D000482	a	http://bioguide.congress.gov/bioguide/photo/D/D000482.jpg	\N
443	Charles	Dent	PA	15	PA15	R	h	\N	\N	\N	2211 Rayburn House Office Building Washington DC, 20515	(202) 225-6411	D000604	a	http://bioguide.congress.gov/bioguide/photo/D/D000604.jpg	\N
445	Matt	Cartwright	PA	17	PA17	D	h	\N	\N	\N	1419 Cannon House Office Building Washington DC, 20515	(202) 225-5546	C001090	a	http://bioguide.congress.gov/bioguide/photo/C/C001090.jpg	\N
446	Tim	Murphy	PA	18	PA18	R	h	\N	\N	\N	2332 Rayburn House Office Building Washington DC, 20515	(202) 225-2301	M001151	a	http://bioguide.congress.gov/bioguide/photo/M/M001151.jpg	\N
449	James	Langevin	RI	2	RI02	D	h	\N	\N	\N	109 Longworth House Office Building Washington DC, 20515	(202) 225-2735	L000559	a	http://bioguide.congress.gov/bioguide/photo/L/L000559.jpg	\N
450	Mark	Sanford	SC	1	SC01	R	h	\N	\N	\N	2201 Rayburn House Office Building Washington DC, 20515	(202) 225-3176	S000051	a	http://bioguide.congress.gov/bioguide/photo/S/S000051.jpg	\N
451	Joe	Wilson	SC	2	SC02	R	h	\N	\N	\N	2229 Rayburn House Office Building Washington DC, 20515	(202) 225-2452	W000795	a	http://bioguide.congress.gov/bioguide/photo/W/W000795.jpg	\N
452	Jeff	Duncan	SC	3	SC03	R	h	\N	\N	\N	106 Longworth House Office Building Washington DC, 20515	(202) 225-5301	D000615	a	http://bioguide.congress.gov/bioguide/photo/D/D000615.jpg	\N
453	Trey	Gowdy	SC	4	SC04	R	h	\N	\N	\N	1404 Cannon House Office Building Washington DC, 20515	(202) 225-6030	G000566	a	http://bioguide.congress.gov/bioguide/photo/G/G000566.jpg	\N
454	Mick	Mulvaney	SC	5	SC05	R	h	\N	\N	\N	2419 Rayburn House Office Building Washington DC, 20515	(202) 225-5501	M001182	a	http://bioguide.congress.gov/bioguide/photo/M/M001182.jpg	\N
455	James	Clyburn	SC	6	SC06	D	h	\N	\N	\N	242 Longworth House Office Building Washington DC, 20515	(202) 225-3315	C000537	a	http://bioguide.congress.gov/bioguide/photo/C/C000537.jpg	\N
456	Tom	Rice	SC	7	SC07	R	h	\N	\N	\N	223 Longworth House Office Building Washington DC, 20515	(202) 225-9895	R000597	a	http://bioguide.congress.gov/bioguide/photo/R/R000597.jpg	\N
457	Kristi	Noem	SD	0	SD00	R	h	\N	\N	\N	2422 Rayburn House Office Building Washington DC, 20515	(202) 225-2801	N000184	a	http://bioguide.congress.gov/bioguide/photo/N/N000184.jpg	\N
458	David	Roe	TN	1	TN01	R	h	\N	\N	\N	407 Longworth House Office Building Washington DC, 20515	(202) 225-6356	R000582	a	http://bioguide.congress.gov/bioguide/photo/R/R000582.jpg	\N
459	John	Duncan	TN	2	TN02	R	h	\N	\N	\N	2207 Rayburn House Office Building Washington DC, 20515	(202) 225-5435	D000533	a	http://bioguide.congress.gov/bioguide/photo/D/D000533.jpg	\N
460	Charles	Fleischmann	TN	3	TN03	R	h	\N	\N	\N	230 Longworth House Office Building Washington DC, 20515	(202) 225-3271	F000459	a	http://bioguide.congress.gov/bioguide/photo/F/F000459.jpg	\N
461	Scott	DesJarlais	TN	4	TN04	R	h	\N	\N	\N	413 Longworth House Office Building Washington DC, 20515	(202) 225-6831	D000616	a	http://bioguide.congress.gov/bioguide/photo/D/D000616.jpg	\N
462	Jim	Cooper	TN	5	TN05	D	h	\N	\N	\N	1536 Cannon House Office Building Washington DC, 20515	(202) 225-4311	C000754	a	http://bioguide.congress.gov/bioguide/photo/C/C000754.jpg	\N
464	Marsha	Blackburn	TN	7	TN07	R	h	\N	\N	\N	2266 Rayburn House Office Building Washington DC, 20515	(202) 225-2811	B001243	a	http://bioguide.congress.gov/bioguide/photo/B/B001243.jpg	\N
466	Steve	Cohen	TN	9	TN09	D	h	\N	\N	\N	2404 Rayburn House Office Building Washington DC, 20515	(202) 225-3265	C001068	a	http://bioguide.congress.gov/bioguide/photo/C/C001068.jpg	\N
467	Louie	Gohmert	TX	1	TX01	R	h	\N	\N	\N	2243 Rayburn House Office Building Washington DC, 20515	(202) 225-3035	G000552	a	http://bioguide.congress.gov/bioguide/photo/G/G000552.jpg	\N
468	Ted	Poe	TX	2	TX02	R	h	\N	\N	\N	2412 Rayburn House Office Building Washington DC, 20515	(202) 225-6565	P000592	a	http://bioguide.congress.gov/bioguide/photo/P/P000592.jpg	\N
469	Sam	Johnson	TX	3	TX03	R	h	\N	\N	\N	2304 Rayburn House Office Building Washington DC, 20515	(202) 225-4201	J000174	a	http://bioguide.congress.gov/bioguide/photo/J/J000174.jpg	\N
471	Jeb	Hensarling	TX	5	TX05	R	h	\N	\N	\N	2228 Rayburn House Office Building Washington DC, 20515	(202) 225-3484	H001036	a	http://bioguide.congress.gov/bioguide/photo/H/H001036.jpg	\N
472	Joe	Barton	TX	6	TX06	R	h	\N	\N	\N	2107 Rayburn House Office Building Washington DC, 20515	(202) 225-2002	B000213	a	http://bioguide.congress.gov/bioguide/photo/B/B000213.jpg	\N
473	John	Culberson	TX	7	TX07	R	h	\N	\N	\N	2372 Rayburn House Office Building Washington DC, 20515	(202) 225-2571	C001048	a	http://bioguide.congress.gov/bioguide/photo/C/C001048.jpg	\N
474	Kevin	Brady	TX	8	TX08	R	h	\N	\N	\N	301 Longworth House Office Building Washington DC, 20515	(202) 225-4901	B000755	a	http://bioguide.congress.gov/bioguide/photo/B/B000755.jpg	\N
475	Al	Green	TX	9	TX09	D	h	\N	\N	\N	2347 Rayburn House Office Building Washington DC, 20515	(202) 225-7508	G000553	a	http://bioguide.congress.gov/bioguide/photo/G/G000553.jpg	\N
476	Michael	McCaul	TX	10	TX10	R	h	\N	\N	\N	131 Longworth House Office Building Washington DC, 20515	(202) 225-2401	M001157	a	http://bioguide.congress.gov/bioguide/photo/M/M001157.jpg	\N
477	K.	Conaway	TX	11	TX11	R	h	\N	\N	\N	2430 Rayburn House Office Building Washington DC, 20515	(202) 225-3605	C001062	a	http://bioguide.congress.gov/bioguide/photo/C/C001062.jpg	\N
478	Kay	Granger	TX	12	TX12	R	h	\N	\N	\N	1026 Cannon House Office Building Washington DC, 20515	(202) 225-5071	G000377	a	http://bioguide.congress.gov/bioguide/photo/G/G000377.jpg	\N
479	Mac	Thornberry	TX	13	TX13	R	h	\N	\N	\N	2208 Rayburn House Office Building Washington DC, 20515	(202) 225-3706	T000238	a	http://bioguide.congress.gov/bioguide/photo/T/T000238.jpg	\N
480	Randy	Weber	TX	14	TX14	R	h	\N	\N	\N	510 Longworth House Office Building Washington DC, 20515	(202) 225-2831	W000814	a	http://bioguide.congress.gov/bioguide/photo/W/W000814.jpg	\N
482	Beto	O'Rourke	TX	16	TX16	D	h	\N	\N	\N	1330 Cannon House Office Building Washington DC, 20515	(202) 225-4831	O000170	a	http://bioguide.congress.gov/bioguide/photo/O/O000170.jpg	\N
483	Bill	Flores	TX	17	TX17	R	h	\N	\N	\N	1030 Cannon House Office Building Washington DC, 20515	(202) 225-6105	F000461	a	http://bioguide.congress.gov/bioguide/photo/F/F000461.jpg	\N
484	Sheila	Jackson Lee	TX	18	TX18	D	h	\N	\N	\N	2252 Rayburn House Office Building Washington DC, 20515	(202) 225-3816	J000032	a	http://bioguide.congress.gov/bioguide/photo/J/J000032.jpg	\N
486	Joaquin	Castro	TX	20	TX20	D	h	\N	\N	\N	212 Longworth House Office Building Washington DC, 20515	(202) 225-3236	C001091	a	http://bioguide.congress.gov/bioguide/photo/C/C001091.jpg	\N
487	Lamar	Smith	TX	21	TX21	R	h	\N	\N	\N	2409 Rayburn House Office Building Washington DC, 20515	(202) 225-4236	S000583	a	http://bioguide.congress.gov/bioguide/photo/S/S000583.jpg	\N
488	Pete	Olson	TX	22	TX22	R	h	\N	\N	\N	2133 Rayburn House Office Building Washington DC, 20515	(202) 225-5951	O000168	a	http://bioguide.congress.gov/bioguide/photo/O/O000168.jpg	\N
490	Kenny	Marchant	TX	24	TX24	R	h	\N	\N	\N	2313 Rayburn House Office Building Washington DC, 20515	(202) 225-6605	M001158	a	http://bioguide.congress.gov/bioguide/photo/M/M001158.jpg	\N
491	Roger	Williams	TX	25	TX25	R	h	\N	\N	\N	1323 Cannon House Office Building Washington DC, 20515	(202) 225-9896	W000816	a	http://bioguide.congress.gov/bioguide/photo/W/W000816.jpg	\N
492	Michael	Burgess	TX	26	TX26	R	h	\N	\N	\N	2336 Rayburn House Office Building Washington DC, 20515	(202) 225-7772	B001248	a	http://bioguide.congress.gov/bioguide/photo/B/B001248.jpg	\N
493	Blake	Farenthold	TX	27	TX27	R	h	\N	\N	\N	1027 Cannon House Office Building Washington DC, 20515	(202) 225-7742	F000460	a	http://bioguide.congress.gov/bioguide/photo/F/F000460.jpg	\N
494	Henry	Cuellar	TX	28	TX28	D	h	\N	\N	\N	2209 Rayburn House Office Building Washington DC, 20515	(202) 225-1640	C001063	a	http://bioguide.congress.gov/bioguide/photo/C/C001063.jpg	\N
495	Gene	Green	TX	29	TX29	D	h	\N	\N	\N	2470 Rayburn House Office Building Washington DC, 20515	(202) 225-1688	G000410	a	http://bioguide.congress.gov/bioguide/photo/G/G000410.jpg	\N
496	Eddie	Johnson	TX	30	TX30	D	h	\N	\N	\N	2468 Rayburn House Office Building Washington DC, 20515	(202) 225-8885	J000126	a	http://bioguide.congress.gov/bioguide/photo/J/J000126.jpg	\N
497	John	Carter	TX	31	TX31	R	h	\N	\N	\N	2110 Rayburn House Office Building Washington DC, 20515	(202) 225-3864	C001051	a	http://bioguide.congress.gov/bioguide/photo/C/C001051.jpg	\N
498	Pete	Sessions	TX	32	TX32	R	h	\N	\N	\N	2233 Rayburn House Office Building Washington DC, 20515	(202) 225-2231	S000250	a	http://bioguide.congress.gov/bioguide/photo/S/S000250.jpg	\N
499	Marc	Veasey	TX	33	TX33	D	h	\N	\N	\N	414 Longworth House Office Building Washington DC, 20515	(202) 225-9897	V000131	a	http://bioguide.congress.gov/bioguide/photo/V/V000131.jpg	\N
500	Filemon	Vela	TX	34	TX34	D	h	\N	\N	\N	437 Longworth House Office Building Washington DC, 20515	(202) 225-9901	V000132	a	http://bioguide.congress.gov/bioguide/photo/V/V000132.jpg	\N
501	Lloyd	Doggett	TX	35	TX35	D	h	\N	\N	\N	2307 Rayburn House Office Building Washington DC, 20515	(202) 225-4865	D000399	a	http://bioguide.congress.gov/bioguide/photo/D/D000399.jpg	\N
502	Brian	Babin	TX	36	TX36	R	h	\N	\N	\N	316 Longworth House Office Building Washington DC, 20515	(202) 225-1555	B001291	a	http://bioguide.congress.gov/bioguide/photo/B/B001291.jpg	\N
503	Rob	Bishop	UT	1	UT01	R	h	\N	\N	\N	123 Longworth House Office Building Washington DC, 20515	(202) 225-0453	B001250	a	http://bioguide.congress.gov/bioguide/photo/B/B001250.jpg	\N
504	Chris	Stewart	UT	2	UT02	R	h	\N	\N	\N	323 Longworth House Office Building Washington DC, 20515	(202) 225-9730	S001192	a	http://bioguide.congress.gov/bioguide/photo/S/S001192.jpg	\N
505	Jason	Chaffetz	UT	3	UT03	R	h	\N	\N	\N	2236 Rayburn House Office Building Washington DC, 20515	(202) 225-7751	C001076	a	http://bioguide.congress.gov/bioguide/photo/C/C001076.jpg	\N
507	Robert	Wittman	VA	1	VA01	R	h	\N	\N	\N	2454 Rayburn House Office Building Washington DC, 20515	(202) 225-4261	W000804	a	http://bioguide.congress.gov/bioguide/photo/W/W000804.jpg	\N
509	Robert	Scott	VA	3	VA03	D	h	\N	\N	\N	1201 Cannon House Office Building Washington DC, 20515	(202) 225-8351	S000185	a	http://bioguide.congress.gov/bioguide/photo/S/S000185.jpg	\N
512	Bob	Goodlatte	VA	6	VA06	R	h	\N	\N	\N	2309 Rayburn House Office Building Washington DC, 20515	(202) 225-5431	G000289	a	http://bioguide.congress.gov/bioguide/photo/G/G000289.jpg	\N
514	Donald	Beyer	VA	8	VA08	D	h	\N	\N	\N	431 Longworth House Office Building Washington DC, 20515	(202) 225-4376	B001292	a	http://bioguide.congress.gov/bioguide/photo/B/B001292.jpg	\N
515	H.	Griffith	VA	9	VA09	R	h	\N	\N	\N	1108 Cannon House Office Building Washington DC, 20515	(202) 225-3861	G000568	a	http://bioguide.congress.gov/bioguide/photo/G/G000568.jpg	\N
517	Gerald	Connolly	VA	11	VA11	D	h	\N	\N	\N	2238 Rayburn House Office Building Washington DC, 20515	(202) 225-1492	C001078	a	http://bioguide.congress.gov/bioguide/photo/C/C001078.jpg	\N
519	Peter	Welch	VT	0	VT00	D	h	\N	\N	\N	2303 Rayburn House Office Building Washington DC, 20515	(202) 225-4115	W000800	a	http://bioguide.congress.gov/bioguide/photo/W/W000800.jpg	\N
520	Suzan	DelBene	WA	1	WA01	D	h	\N	\N	\N	318 Longworth House Office Building Washington DC, 20515	(202) 225-6311	D000617	a	http://bioguide.congress.gov/bioguide/photo/D/D000617.jpg	\N
521	Rick	Larsen	WA	2	WA02	D	h	\N	\N	\N	2113 Rayburn House Office Building Washington DC, 20515	(202) 225-2605	L000560	a	http://bioguide.congress.gov/bioguide/photo/L/L000560.jpg	\N
522	Jaime	Herrera Beutler	WA	3	WA03	R	h	\N	\N	\N	1130 Cannon House Office Building Washington DC, 20515	(202) 225-3536	H001056	a	http://bioguide.congress.gov/bioguide/photo/H/H001056.jpg	\N
523	Dan	Newhouse	WA	4	WA04	R	h	\N	\N	\N	1641 Cannon House Office Building Washington DC, 20515	(202) 225-5816	N000189	a	http://bioguide.congress.gov/bioguide/photo/N/N000189.jpg	\N
524	Cathy	McMorris Rodgers	WA	5	WA05	R	h	\N	\N	\N	203 Longworth House Office Building Washington DC, 20515	(202) 225-2006	M001159	a	http://bioguide.congress.gov/bioguide/photo/M/M001159.jpg	\N
525	Derek	Kilmer	WA	6	WA06	D	h	\N	\N	\N	1520 Cannon House Office Building Washington DC, 20515	(202) 225-5916	K000381	a	http://bioguide.congress.gov/bioguide/photo/K/K000381.jpg	\N
527	David	Reichert	WA	8	WA08	R	h	\N	\N	\N	1127 Cannon House Office Building Washington DC, 20515	(202) 225-7761	R000578	a	http://bioguide.congress.gov/bioguide/photo/R/R000578.jpg	\N
528	Adam	Smith	WA	9	WA09	D	h	\N	\N	\N	2264 Rayburn House Office Building Washington DC, 20515	(202) 225-8901	S000510	a	http://bioguide.congress.gov/bioguide/photo/S/S000510.jpg	\N
529	Denny	Heck	WA	10	WA10	D	h	\N	\N	\N	425 Longworth House Office Building Washington DC, 20515	(202) 225-9740	H001064	a	http://bioguide.congress.gov/bioguide/photo/H/H001064.jpg	\N
530	Paul	Ryan	WI	1	WI01	R	h	\N	\N	\N	1233 Cannon House Office Building Washington DC, 20515	(202) 225-3031	R000570	a	http://bioguide.congress.gov/bioguide/photo/R/R000570.jpg	\N
531	Mark	Pocan	WI	2	WI02	D	h	\N	\N	\N	313 Longworth House Office Building Washington DC, 20515	(202) 225-2906	P000607	a	http://bioguide.congress.gov/bioguide/photo/P/P000607.jpg	\N
532	Ron	Kind	WI	3	WI03	D	h	\N	\N	\N	1502 Cannon House Office Building Washington DC, 20515	(202) 225-5506	K000188	a	http://bioguide.congress.gov/bioguide/photo/K/K000188.jpg	\N
533	Gwen	Moore	WI	4	WI04	D	h	\N	\N	\N	2245 Rayburn House Office Building Washington DC, 20515	(202) 225-4572	M001160	a	http://bioguide.congress.gov/bioguide/photo/M/M001160.jpg	\N
534	F.	Sensenbrenner	WI	5	WI05	R	h	\N	\N	\N	2449 Rayburn House Office Building Washington DC, 20515	(202) 225-5101	S000244	a	http://bioguide.congress.gov/bioguide/photo/S/S000244.jpg	\N
535	Glenn	Grothman	WI	6	WI06	R	h	\N	\N	\N	501 Longworth House Office Building Washington DC, 20515	(202) 225-2476	G000576	a	http://bioguide.congress.gov/bioguide/photo/G/G000576.jpg	\N
536	Sean	Duffy	WI	7	WI07	R	h	\N	\N	\N	1208 Cannon House Office Building Washington DC, 20515	(202) 225-3365	D000614	a	http://bioguide.congress.gov/bioguide/photo/D/D000614.jpg	\N
538	David	McKinley	WV	1	WV01	R	h	\N	\N	\N	412 Longworth House Office Building Washington DC, 20515	(202) 225-4172	M001180	a	http://bioguide.congress.gov/bioguide/photo/M/M001180.jpg	\N
539	Alexander	Mooney	WV	2	WV02	R	h	\N	\N	\N	1232 Cannon House Office Building Washington DC, 20515	(202) 225-2711	M001195	a	http://bioguide.congress.gov/bioguide/photo/M/M001195.jpg	\N
541	Cynthia	Lummis	WY	0	WY00	R	h	\N	\N	\N	2433 Rayburn House Office Building Washington DC, 20515	(202) 225-2311	L000571	r	http://bioguide.congress.gov/bioguide/photo/L/L000571.jpg	Announced retirement on Nov. 12, 2015
\.


--
-- Name: rep_rep_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jonathangoldman
--

SELECT pg_catalog.setval('rep_rep_id_seq', 541, true);


--
-- Name: rep_pkey; Type: CONSTRAINT; Schema: public; Owner: jonathangoldman; Tablespace: 
--

ALTER TABLE ONLY rep
    ADD CONSTRAINT rep_pkey PRIMARY KEY (rep_id);


--
-- Name: idx_rep_status; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX idx_rep_status ON rep USING btree (status);


--
-- Name: ix_rep_chamber; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX ix_rep_chamber ON rep USING btree (chamber);


--
-- Name: ix_rep_district_code; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX ix_rep_district_code ON rep USING btree (district_code);


--
-- Name: ix_rep_district_number; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX ix_rep_district_number ON rep USING btree (district_number);


--
-- Name: ix_rep_party_code; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX ix_rep_party_code ON rep USING btree (party_code);


--
-- Name: ix_rep_state_code; Type: INDEX; Schema: public; Owner: jonathangoldman; Tablespace: 
--

CREATE INDEX ix_rep_state_code ON rep USING btree (state_code);


--
-- PostgreSQL database dump complete
--

