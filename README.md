# 🌀 Stable-Fast-3D Inference Script

이 저장소는 [**Stable Fast 3D**](https://huggingface.co/stabilityai/stable-fast-3d) 모델을 활용하여 **2D 인물 이미지로부터 3D 메쉬(.glb)** 를 생성하는 파이프라인을 제공합니다.  
배경 제거, 전처리, 모델 추론 및 메쉬 저장까지 한번에 수행할 수 있습니다.

## 🔧 설치 방법

```bash
git clone https://github.com/<your-org-or-username>/stable-fast-3d-inference.git
cd stable-fast-3d-inference
python -m venv env
source env/bin/activate   # on Windows: env\Scripts\activate
pip install -r requirements.txt
```

### ⚠️ 요구사항
- Python 3.9+
- PyTorch >= 2.0
- rembg
- PIL, tqdm 등

## 🚀 사용법

```bash
python run.py path/to/image_or_folder \
  --device cuda \
  --pretrained-model stabilityai/stable-fast-3d \
  --foreground-ratio 0.85 \
  --output-dir output/ \
  --texture-resolution 1024 \
  --remesh_option none \
  --target_vertex_count -1 \
  --batch_size 1
```

### 주요 인자 설명
| 옵션 | 설명 | 기본값 |
|--------|-------|--------|
| `image` | 입력 이미지 또는 폴더 경로 | 필수 |
| `--device` | `cuda`, `mps`, 또는 `cpu` | 자동 탐지 |
| `--pretrained-model` | Huggingface 모델 ID 또는 로컬 경로 | `stabilityai/stable-fast-3d` |
| `--foreground-ratio` | 전경 크기를 조절하는 비율 (0~1) | 0.85 |
| `--output-dir` | 결과물 저장 디렉토리 | `output/` |
| `--texture-resolution` | 텍스처 맵 해상도 | 1024 |
| `--remesh_option` | 메쉬 리메싱 옵션 (`none`, `triangle`, `quad`) | `none` |
| `--target_vertex_count` | 리덕션 대상 정점 수 (-1: 비활성화) | -1 |
| `--batch_size` | 배치 사이즈 | 1 |

## 🖼️ 출력 예시

- `output/0/input.png`: 전처리된 입력 이미지
- `output/0/mesh.glb`: 생성된 3D 메쉬 파일 (GLB 포맷)

## 🧠 동작 방식

1. rembg를 통해 배경 제거
2. 설정된 전경 비율로 리사이즈
3. Stable-Fast-3D 모델로 3D 메쉬 생성
4. glTF(.glb) 형식으로 결과 저장

## 📌 참고 및 출처

- 모델 출처: [Stability AI - stable-fast-3d](https://huggingface.co/stabilityai/stable-fast-3d)
- 코드 일부는 `sf3d.system`, `sf3d.utils` 모듈에 기반하여 작성되었습니다.
- rembg 배경 제거 기능은 [danielgatis/rembg](https://github.com/danielgatis/rembg) 프로젝트를 사용합니다.
