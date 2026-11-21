"""Edited English news copy. Story numbers map to SOURCES.md.
Only Friday events or newly reported Friday developments are included.
"""
DATE = "Friday, 20 November 2026"
STORIES = [
    (1, "LEAD", "After the genocide ruling: a road home?", "Bangladesh sets a return goal; Myanmar rejects ICJ finding.", 92, 22),
    (2, "ASIA", "China–Indonesia trade talks launched", "Xi and Prabowo open partnership talks in Shenzhen.", 114, 23),
    (3, "OCEANIA", "Xi hails Australia ties' turnaround", "Albanese meets China's leader in Shenzhen on Friday.", 151, -34),
    (4, "ASIA", "Taiwan flags 2,700 suspected fake accounts", "Taiwan alleges China links; Meta denies election posts.", 121, 24),
    (5, "ASIA", "Jakarta questions YouTube removals", "Indonesia asks Google to explain 19,000 channel bans.", 107, -6),
    (6, "ASIA", "Cyclone Akvan makes landfall", "Storm crosses Odisha's coast near Gopalpur, India.", 85, 19),
    (7, "ECONOMY / TECHNOLOGY", "India proposes exchange governance limits", "SEBI seeks lower director age caps and shorter tenures.", 73, 19),
    (8, "ASIA", "Tamil Nadu drops airport plan", "State tells court Parandur project faces waterbody risks.", 80, 13),
    (9, "ASIA", "Andhra explores small nuclear reactors", "Indian state clears APGenco to study SMR power sites.", 80, 16),
    (10, "OCEANIA", "Sydney raids: three men charged", "Police allege terror-material offences against one man.", 151, -34),
    (11, "OCEANIA", "NZ defence sites hit by cyber breach", "NZDF takes sites offline; family database accessed.", 175, -41),
    (12, "OCEANIA", "Whale-stranding toll rises to 22", "Three more sperm whales die at NZ's Ninety Mile Beach.", 173, -35),
    (13, "OCEANIA", "Cook Islands mobilises cyclone relief", "Vessels await safe passage as Xavier falls to Category 2.", -159, -21),
    (14, "MIDDLE EAST", "Saudi coalition strikes Hodeidah", "Yemen's Houthis warn airlines to avoid Saudi airspace.", 43, 15),
    (15, "MIDDLE EAST", "Iraqi troops enter militia stronghold", "Forces deploy to Jurf al-Sakhar under a compromise.", 44, 33),
    (16, "MIDDLE EAST", "Tanker hit in Strait of Hormuz", "Unknown projectile starts fire near Khasab, Oman.", 56, 27),
    (17, "MIDDLE EAST", "Gaza reports six killed in strikes", "Civil defence gives Friday toll; Israel says militants hit.", 34, 31),
    (18, "AFRICA", "Angola oil plan gets $4bn approval", "Exxon and partners back offshore Kizomba redevelopment.", 12, -7),
    (19, "AFRICA", "Angola prices planned De Beers stake", "Endiama CEO says 10% diamond-company stake costs $180m.", 13, -9),
    (20, "GLOBAL / HUMANITARIAN", "WFP cuts reach as hunger crisis looms", "UN seeks $12.1bn to feed 91 million people in 2027.", 12, 42),
    (21, "MIDDLE EAST", "COP31 enters overtime in Antalya", "Countries remain split on draft omitting fossil fuels.", 31, 37),
    (22, "EUROPE", "UK and EU conclude reset talks", "Brussels summit seals youth, food-trade and carbon plans.", 4, 51),
    (23, "EUROPE", "Russian weapons enter Polish airspace", "Warsaw activates defences; no injuries are reported.", 23, 51),
    (24, "EUROPE", "Russian barrage kills at least nine", "Overnight attack damages three bridges in Kyiv, Ukraine.", 30, 50),
    (25, "EUROPE", "Estonia approves Russian border closure", "All road crossings to shut from 1 December after sabotage.", 26, 59),
    (26, "EUROPE", "Denmark expels Russian defence attaché", "Copenhagen alleges a plot to kill a Ukrainian rapper.", 13, 56),
    (27, "EUROPE", "Europe's workers and students protest", "Rallies demand better pay and services in 25+ countries.", 12, 42),
    (28, "EUROPE", "Amnesty faults Spain's strike policing", "New report alleges excessive force at 11 November protests.", -4, 40),
    (29, "AMERICAS", "Judge blocks Trump's proposed arch", "Virginia judge says rushed Washington project lacks basis.", -77, 39),
    (30, "AMERICAS", "Florida river rises above record", "St. Johns reaches nearly 18.7 feet near flooded Cocoa.", -81, 28),
    (31, "AMERICAS", "Halifax security forum opens", "Canadian-hosted talks focus on Ukraine and allied defence.", -64, 45),
    (32, "AMERICAS", "Mexico marks Revolution anniversary", "Sheinbaum defends 2027 voting process at military parade.", -99, 19),
    (33, "AMERICAS", "Magnitude-6.7 quake hits central Peru", "Peru's IGP places epicentre northwest of Junín on Friday.", -76, -11),
    (34, "ECONOMY / TECHNOLOGY", "Trump threatens offshore data-centre tax", "US firms building abroad face proposed penalties, not law.", -77, 39),
    (35, "ECONOMY / TECHNOLOGY", "Tech rout sinks Wall Street", "Nasdaq closes down 5.28%; S&P 500 loses 3.7% Friday.", -74, 41),
    (36, "ECONOMY / TECHNOLOGY", "Fed's Cook urges further rate rises", "US governor warns inflation may demand more tightening.", -71, -33),
    (37, "ECONOMY / TECHNOLOGY", "UK retail sales rebound 0.7%", "Friday ONS release reports an October rise in volumes.", 0, 52),
    (38, "ECONOMY / TECHNOLOGY", "Canadian retail sales rise 0.8%", "New September figures put sales at C$75.3 billion.", -76, 45),
    (39, "ECONOMY / TECHNOLOGY", "US consumer sentiment improves", "Final November survey: 51.5; year-ahead inflation 3.7%.", -84, 42),
]

assert len(STORIES) == 39
assert len({story[0] for story in STORIES}) == len(STORIES)
