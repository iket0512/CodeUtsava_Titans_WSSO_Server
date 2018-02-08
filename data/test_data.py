import csv

element_data = [
{
	"name" : "Iron",
	"hazards" : "Iron in water affects both beverages and food. It causes the water to taste harshly, metallically offensive, and the taste carries into coffee, tea and other beverages made with iron-laden water. Aside from bad taste, iron adds an unpleasant, inky blackness to beverages. Food, especially vegetables, cooked in well water containing iron turns unappetizingly dark and absorbs the taste of the water. Effects on Your Health:While a low level of iron isn't harmful in and of itself, iron in drinking water is classified as a secondary contaminant according to the EPA. This is because iron often carries with it bacteria that feed off the iron to survive. These small organisms can be harmful when digested.In addition, if your iron levels are too high, serious health effects can develop, including iron overload.Effects on Your Skin:Water with excessive amounts of dissolved minerals such as iron and magnesium can have negative effects on your skin. They can damage healthy skin cells, which can lead to wrinkles.",
	"remedy" : "Aeration:This method adds oxygen to the water to oxidize the iron.Oxidizing Filter: This causes immediate oxidation and adds a reverse (backwash) flush system.Water Softener:Designed to remove minerals that cause hard water, softeners do remove small amounts of iron.",
	"permissible_limit_low": .30,
	"permissible_limit_high": 1.0
},{
	"name":"Arsenic",
	"hazards":"Acute effects:The immediate symptoms of acute arsenic poisoning include vomiting, abdominal pain and diarrhoea. These are followed by numbness and tingling of the extremities, muscle cramping and death, in extreme cases.Long-term effects:The first symptoms of long-term exposure to high levels of inorganic arsenic are usually observed in the skin, and include pigmentation changes, skin lesions and hard patches on the palms and soles of the feet .These occur after a minimum exposure of approximately five years and may be a precursor to skin cancer.In addition to skin cancer, long-term exposure to arsenic may also cause cancers of the bladder and lungs. The International Agency for Research on Cancer (IARC) has classified arsenic and arsenic compounds as carcinogenic to humans, and has also stated that arsenic in drinking-water is carcinogenic to humans.",
	"remedy" : "Substitute high-arsenic sources, such as groundwater, with low-arsenic, microbiologically safe sources such as rain water and treated surface water. Low-arsenic water can be used for drinking, cooking and irrigation purposes, whereas high-arsenic water can be used for other purposes such as bathing and washing clothes.Discriminate between high-arsenic and low-arsenic sources. For example, test water for arsenic levels and paint tube wells or hand pumps different colours. This can be an effective and low-cost means to rapidly reduce exposure to arsenic when accompanied by effective education.Blend low-arsenic water with higher-arsenic water to achieve an acceptable arsenic concentration level.Install arsenic removal systems - either centralized or domestic - and ensure the appropriate disposal of the removed arsenic. Technologies for arsenic removal include oxidation, coagulation-precipitation, absorption, ion exchange, and membrane techniques. There is an increasing number of effective and low-cost options for removing arsenic from small or household supplies, though there is still limited evidence about the extent to which such systems are used effectively over sustained periods of time.",
	"permissible_limit_low": .01,
	"permissible_limit_high": .05
},{
	"name":"Fluoride",
	"hazards":"Ingestion of excess fluoride, most commonly in drinking-water, can cause fluorosis which affects the teeth and bones. Moderate amounts lead to dental effects, but long-term ingestion of large amounts can lead to potentially severe skeletal problems.Acute high-level exposure to fluoride causes immediate effects of abdominal pain, excessive saliva, nausea and vomiting. Seizures and muscle spasms may also occur.The margin between the toxic and therapeutic dose is very narrow",
	"remedy":"Reverse Osmosis Filtration - This is used to purify several types of bottled water (not all), so some bottled waters are unfluoridated. Reverse osmosis systems are generally unaffordable for personal use.Activated Alumina Defluoridation Filter - These filters are used in locales where fluorosis is prevalent. They are relatively expensive (lowest price I saw was $30/filter) and require frequent replacement, but do offer an option for home water filtration.Distillation Filtration - There are commercially available distillation filters that can be purchased to remove fluoride from water.",
	"permissible_limit_low": 1.0,
	"permissible_limit_high": 1.50
},{
	"name":"Nitrate",
	"remedy":"Reverse Osmosis is often a point of use application that is known to successfully remove 83-92 percent of nitrates in water thus being well within acceptable levels. Along with nitrate/nitrite removal, reverse osmosis technology can remove a variety of other impurities in your water including organics, inorganics, bacteria, and particulates.Ion Exchange: Another choice to address nitrate issues is ion exchange technology. WaterTech's NitroMAX, a whole-house ion exchange water conditioner, effectively reduces and removes nitrates while simultaneously reducing water hardness and preventing scale buildup throughout the home. When you remove nitrates from your water, you immediately boost your water quality, making the water flowing through your home better for you and your family. Learn more about WaterTech's NitroMax system by talking with an authorized WaterTech dealer in your area today.",
	"hazards":"Too much nitrate in drinking water poses a risk to infants under six months of age. If an infant is fed water or formula made with water that is high in nitrate, a condition called 'blue baby syndrome' (or 'methemoglobinemia') can develop. Bacteria which are present in an infant's stomach can convert nitrate to nitrite (NO2), a chemical which can interfere with the ability of the infant's blood to carry oxygen. As the condition worsens, the baby's skin turns a bluish color, particularly around the eyes and mouth. If nitrate levels in the water are high enough and prompt medical attention is not received, death can result.",
	"permissible_limit_low": 45.00,
	"permissible_limit_high": 45.00
},{
	"name":"Salinity",
	"hazards":"Agricultural production:If the level of salts in the soil water is too high, water may flow from the plant roots back into the soil. This results in dehydration of the plant, causing yield decline or even death of the plant.Water quality:The most significant off-site impact of dryland salinity is the salinisation of previously fresh rivers. This affects the quality of water for drinking and irrigation-with serious economic, social and environmental consequences for both rural and urban communities.High blood pressure is a leading cause of cardiovascular disease. It accounts for two-thirds of all strokes and half of heart disease.In China, high blood pressure is the leading cause of preventable death, responsible for more than one million deaths a year.",
	"remedy":"Reverse osmosis: In a reverse osmosis filtration system, water flows through a membrane, filtering out some of the molecules within the water, including sodium and chloride. These molecules, plus some water, are flushed into your home's wastewater system. The treated water is stored in a small storage tank until needed. This system can be installed at the point-of-use, such as at the kitchen sink, or could be used to treat the water for your whole house.Distillation: A distillation system uses temperature change to evaporate and recondense clean water. Inorganic minerals, such as sodium and chloride, do not usually transfer into the condensed water, but some organic contaminants will. These systems are installed either under the sink or counter and can increase a home's energy costs.De-ionization: Similar to a water softener, in a deionization system water is filtered through a resin, but acids and bases are used rather than salt to regenerate the system. While it is effective, there are some hazardous chemicals required in running the system.",
	"permissible_limit_low": 1800,
	"permissible_limit_high": 2000
}]

def load_data():
	data = []
	heads = ["sno","state","district","block","panchayat","village","habitation","element","limit","count","status"]
	file = open('contaminated_data.csv', 'r')
	reader = csv.reader(file)
	for line in reader:
		tmp = {}
		i = 0
		for head in heads:
			tmp[head] = line[i]
			i = i + 1
		data.append(tmp)
	return data