class TDEE(object):
    """Calculates TDEE (Total Daily Energy Expenditure).
    TDEE is calculating based on 'The Mifflin St Jeor Equation': TDEE = BMR + TEA + EPOC + TEF + NEAT:
        BMR  - Basal Metabolic Rate
        TEA  - Thermic Effect Of Activity
        EPOC - Excess Post-exercise Oxygen Consumption
        TEF  - Thermic Effect of Food
        NEAT - Non-Exercise Activity Thermogenesis
    """
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'

    BODY_ECTOMORPHIC = 'ecto'
    BODY_MESOMORPHIC = 'meso'
    BODY_ENDOMORPHIC = 'endo'

    INTENSITY_LOW = 'l'
    INTENSITY_MEDIUM = 'm'
    INTENSITY_HEIGHT = 'h'

    WORKOUT_STRENGTH = 'strength'
    WORKOUT_AEROBIC = 'aerobic'

    NEAT_VALUES = {
        BODY_ECTOMORPHIC: [700, 800, 900],
        BODY_MESOMORPHIC: [400, 450, 500],
        BODY_ENDOMORPHIC: [200, 300, 400]
    }

    TEA_KCAL_FACTORS = {
        WORKOUT_STRENGTH: {INTENSITY_LOW: 7, INTENSITY_MEDIUM: 8, INTENSITY_HEIGHT: 9},
        WORKOUT_AEROBIC: {INTENSITY_LOW: 5, INTENSITY_MEDIUM: 7, INTENSITY_HEIGHT: 10}
    }

    EPOC_KCAL_FACTORS = {
        WORKOUT_STRENGTH: {INTENSITY_LOW: 0.04, INTENSITY_MEDIUM: 0.05, INTENSITY_HEIGHT: 0.07},
        WORKOUT_AEROBIC: {INTENSITY_LOW: 5, INTENSITY_MEDIUM: 35, INTENSITY_HEIGHT: 180}
    }

    S_FACTOR = {GENDER_MALE: 5, GENDER_FEMALE: -161}

    def __init__(self, age, height, weight, gender, body_type,
                 strength_time, strength_frequency, strength_intensity,
                 aerobic_time, aerobic_frequency, aerobic_intensity):
        """
        Args:
            age:
                Age in years.
            height:
                Height in cm.
            weight:
                Weight in kg.
            gender:
                TDEE.GENDER_MALE | TDEE.GENDER_FEMALE.
            body_type:
                TDEE.BODY_ECTOMORPHIC | TDEE.BODY_MESOMORPHIC | TDEE.BODY_ENDOMORPHIC.
            strength_time:
                Time of strength training per day (in minutes).
            strength_frequency:
                Number of trainings per week.
            strength_intensity:
                TDEE.INTENSITY_LOW | TDEE.INTENSITY_MEDIUM | TDEE.INTENSITY_HEIGHT.
            aerobic_time:
                Time of aerobic training per day (in minutes).
            aerobic_frequency:
                Number of trainings per week.
            aerobic_intensity:
                TDEE.INTENSITY_LOW | TDEE.INTENSITY_MEDIUM | TDEE.INTENSITY_HEIGHT.
        """
        if gender not in [TDEE.GENDER_MALE, TDEE.GENDER_FEMALE]:
            raise ValueError('Invalid gender: {0}'.format(gender))

        if body_type not in [TDEE.BODY_ECTOMORPHIC, TDEE.BODY_MESOMORPHIC, TDEE.BODY_ENDOMORPHIC]:
            raise ValueError('Invalid body_type: {0}'.format(body_type))

        if strength_intensity not in [TDEE.INTENSITY_LOW, TDEE.INTENSITY_MEDIUM, TDEE.INTENSITY_HEIGHT]:
            raise ValueError('Invalid strength_intensity: {0}'.format(strength_intensity))

        if aerobic_intensity not in [TDEE.INTENSITY_LOW, TDEE.INTENSITY_MEDIUM, TDEE.INTENSITY_HEIGHT]:
            raise ValueError('Invalid aerobic_intensity: {0}'.format(aerobic_intensity))

        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.body_type = body_type

        self.strength_time = strength_time
        self.strength_frequency = strength_frequency
        self.strength_intensity = strength_intensity

        self.aerobic_time = aerobic_time
        self.aerobic_frequency = aerobic_frequency
        self.aerobic_intensity = aerobic_intensity

    def calculate(self):
        tdee = self.bmr + (self.tea / 7) + self.neat
        tdee += tdee * 0.08  # Adding TEF.
        return int('{0:.0f}'.format(tdee))

    @property
    def bmr(self):
        """Calculates BMR (Basal Metabolic Rate) based on 'The Mifflin St Jeor Equation'."""

        bmr = (9.99 * self.weight) + (6.25 * self.height) - (4.92 * self.age) + self.s_factor
        return int('{0:.0f}'.format(bmr))

    @property
    def tea(self):
        strength_tea = self.strength_frequency * self.strength_time * self.tea_strength_factor
        aerobic_tea = self.aerobic_frequency * self.aerobic_time * self.tea_aerobic_factor

        strength_epoc = self.strength_frequency * (self.epoc_strength_factor * self.bmr)
        aerobic_epoc = self.aerobic_frequency * self.epoc_aerobic_factor

        tea = strength_tea + strength_epoc + aerobic_tea + aerobic_epoc

        return int('{0:.0f}'.format(tea))

    @property
    def neat(self):
        return self.NEAT_VALUES[self.body_type][1]

    ########## FACTORS

    @property
    def tea_strength_factor(self):
        return self.TEA_KCAL_FACTORS[self.WORKOUT_STRENGTH][self.strength_intensity]

    @property
    def tea_aerobic_factor(self):
        return self.TEA_KCAL_FACTORS[self.WORKOUT_AEROBIC][self.aerobic_intensity]

    @property
    def epoc_strength_factor(self):
        return self.EPOC_KCAL_FACTORS[self.WORKOUT_STRENGTH][self.strength_intensity]

    @property
    def epoc_aerobic_factor(self):
        return self.EPOC_KCAL_FACTORS[self.WORKOUT_AEROBIC][self.aerobic_intensity]

    @property
    def s_factor(self):
        return self.S_FACTOR[self.gender]