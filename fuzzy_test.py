from fuzzy_extractor import FuzzyExtractor

extractor = FuzzyExtractor(16, 8)
key, helper = extractor.generate('AABBCCDDEEFFGGHH')

print("KEY: " + str(key))
print(extractor.reproduce('AABBCCDDEEFFGGHH', helper))
print(extractor.reproduce('AABBCXDDEEFFGGHH', helper))
print(extractor.reproduce('VABBCXDDNNFFGGHF', helper))
print(extractor.reproduce('AABBCCDDEEFFGGHI', helper))
print(extractor.reproduce('AAAAAAAAAAAAAAAA', helper))
