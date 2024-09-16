# Dhvani: A Weakly-supervised Phonemic Error Detection and Feedback System for Hindi

## Introduction

Dhvani is a novel Computer-Assisted Pronunciation Training (CAPT) system designed specifically for Hindi, addressing the critical gap in pronunciation tools for Indian languages. With over 500 million Hindi speakers, improving Hindi pronunciation is a vital step toward enhancing communication and connectivity within India's linguistically diverse landscape.

## Key Features

1. **Phonemic Error Detection**: Utilizes a weakly-supervised encoder-decoder structure for accurate detection of pronunciation errors at the phoneme level.
2. **Synthetic Speech Generation**: Implements innovative techniques to create diverse datasets for training, overcoming the scarcity of mispronounced speech data.
3. **Targeted Feedback Mechanism**: Provides detailed, actionable feedback to learners, including instructions on tongue position, lip movement, and teeth placement, supplemented by visual aids.
4. **Hindi-Specific Design**: Leverages Hindi's phonetic nature for more elegant handling of mispronounced speech and addresses challenges faced by diverse linguistic groups.

## Model Architecture

Dhvani's architecture consists of two main components:

1. **R-CNN Mel-Spectrogram Encoder**: Processes input speech through pre-processing to generate a mel-spectrogram, which is then fed into a Recurrent Convolutional Neural Network (RCNN) for feature extraction.

2. **A-RNN Phoneme Decoder**: An Attention-based Recurrent Neural Network (ARNN) that decodes the extracted features into phoneme sequences.

The output is then passed through a Classification Head with 67 units, corresponding to Hindi phonemes and special tokens.

![Our model architecture](model-overall.svg)
![Our feedback system](feedback-mechanism.svg)
## Dataset

The model is trained on a combination of:

1. **MUCS Dataset**: A subset of the Multilingual and Code-switching ASR Challenge dataset, containing 95.05 hours of training data and 5.55 hours of test data from telephone-quality Hindi speech recordings.

2. **Synthetic Dataset**: Over 3 hours of synthetic Hindi speech generated using the suno/bark-small text-to-speech model, comprising 1,000 correctly pronounced and 1,000 mispronounced sentence pairs.

## Performance

Dhvani demonstrates significant improvements over existing CAPT systems:

- **Recall**: 75.48%
- **Precision**: 89.94%
- **F-measure**: 82.24%

These results set a new benchmark for Hindi pronunciation training.

## Feedback Mechanism

Dhvani provides comprehensive phonetic feedback covering the full range of Hindi phonology:

- Detailed articulatory guidance for each phoneme
- Visual aids including tongue diagrams
- Comparisons to English phonemes for non-native speakers
- Special attention to challenging aspects like retroflex and aspirated consonants

## Example Phoneme Feedback

### Sentence:
**"घड़ी में ढोलक का ध्वनि सुनाई दिया।"**  
(Translation: "The sound of the drum was heard from the clock.")

## Phoneme Feedback:

### 1. Phoneme: घ (gha)
- **Tongue position**: The back of the tongue should touch the soft palate.
- **Lip movement**: Lips remain slightly apart, do not touch.
- **Teeth placement**: Upper and lower teeth are apart.
- **Common mistake**: Confusing घ (gha) with ग (ga) by not adding enough aspiration.
  
![Tongue Diagram for घ (gha)](feedback-mechanism-2.png)

---

### 2. Phoneme: ध (dha)
- **Tongue position**: The tip of the tongue touches the alveolar ridge (just behind the upper front teeth).
- **Lip movement**: Lips remain relaxed.
- **Teeth placement**: Teeth remain apart.
- **Common mistake**: Under-aspiration or blending with द (da).

![Tongue Diagram for ध (dha)](feedback-mechanism-1.png)

---

### 3. Phoneme: छ (chha)
- **Tongue position**: The front part of the tongue should touch the hard palate.
- **Lip movement**: Lips stay relaxed, slightly apart.
- **Teeth placement**: Upper and lower teeth should not touch.
- **Common mistake**: Confusion with छ (chha) due to under-aspiration.

![Tongue Diagram for च (cha)](feedback-mechanism-11.png)

---

### 4. Phoneme: ढ (dha)
- **Tongue position**: The tongue is curled backward, touching the area just behind the alveolar ridge.
- **Lip movement**: Lips remain relaxed.
- **Teeth placement**: Upper and lower teeth should remain apart.
- **Common mistake**: Incorrect retroflex articulation, blending it with द (da).

![Tongue Diagram for ढ (dha)](feedback-mechanism.png)


## Future Work

The research presents promising avenues for future development:

1. Adaptation to other Indian languages
2. Integration with language learning platforms
3. Enhancement of the feedback system with more interactive elements
4. Exploration of real-time pronunciation correction in conversational settings


