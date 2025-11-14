# Deepfake Detector (free)

*Simple deepfake detection tool using **Reality Defender API**. Works only for audio and image files.*

## Limitations

 - 50 uploads p/mo
 - Audio: .mp3 .wav .m4a .aac .ogg .flac .alac
 - Image: .jpg .jpeg .png .gif .webp

## Setup

- **Clone** the repo
- run **pip install requirements.txt**
- **get** API key from Reality Defender
- create a **.env** file and add your api key in the following format
```text
REALITY_DEFENDER_API_KEY=api-key
```
- **use** the tool...

```bash
python dfd.py <file>
```

## Output

**The tool shows:**

- File name
- Analysis status
- Score (0.0 to 1.0)
- Result interpretation

**Score Guide:**

- Below 0.3 = Likely authentic
- 0.3 to 0.7 = Uncertain
- Above 0.7 = Likely deepfake

**example output**

```bash
==================================================
File: test.jpg
Status: completed
Score: 0.85
ID: abc123...

Model Results:
  model_v1: 0.82 (synthetic)
  model_v2: 0.88 (synthetic)
==================================================
Result: LIKELY DEEPFAKE
```

## Links

- https://www.realitydefender.com/
- https://docs.realitydefender.com/introduction
- https://github.com/Reality-Defender/realitydefender-sdk-python 
