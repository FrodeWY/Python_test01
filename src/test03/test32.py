import json

jsons = '[{"bottomright": {"y": 473, "x": 1182}, "topleft": {"y": 185, "x": 1077}, "confidence": 0.25, "label": "chair"},' \
        '{"bottomright": {"y": 473, "x": 1182}, "topleft": {"y": 185, "x": 1077}, "confidence": 0.25, "label": "chair"}]'

f= json.loads(jsons)
print(f)
for i in f:
    print(i)