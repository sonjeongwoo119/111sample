import streamlit as st
import openai

# -----------------------------
# 📌 사이드바 메뉴
# -----------------------------
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)

# -----------------------------
# 🗂️ 탭 구성
# -----------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🎈 소개",
    "🧱 페이지 구조",
    "🖼️ 이미지",
    "🔗 링크와 열",
    "📁 탭 UI",
    "👤 사용자 입력",
    "📷 카메라",
    "🤖 GPT"
    "음악 추천받기"
])

# -----------------------------
# 🎈 소개 탭
# -----------------------------
with tab1:
    st.title("🎈 손정우의 첫 번째 앱")
    st.info("안녕하세요 반갑습니다. 저는 손정우 입니다.")
    st.write("안녕하세요 반갑습니다. 저는 손정우 입니다")

# -----------------------------
# 🧱 페이지 구조 탭
# -----------------------------
with tab2:
    st.title("위")
    st.header("중간")
    st.subheader("아래")

# -----------------------------
# 🖼️ 이미지 탭
# -----------------------------
with tab3:
    st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWI2Y2l4dmdqOWxnZWplazN5dHQ2bXJubTU4NWEzMmFkaXZjMWJldiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HeiJ27Z2DDrzvrlcW0/giphy.gif")

# -----------------------------
# 🔗 링크와 열 탭
# -----------------------------
with tab4:
    st.title("Hello")
    st.link_button("tetr.io", "https://tetr.io/")

    col1, col2 = st.columns(2)
    with col1:
        st.write("왼쪽 열입니다.")
    with col2:
        st.write("오른쪽 열입니다.")

# -----------------------------
# 📁 탭 UI 탭
# -----------------------------
with tab5:
    inner_tab1, inner_tab2 = st.tabs(["탭 1", "탭 2"])
    with inner_tab1:
        st.write("탭 1111111111111111.")
    with inner_tab2:
        st.write("탭 2222222222222222.")

# -----------------------------
# 👤 사용자 입력 탭
# -----------------------------
with tab6:
    name = st.text_input("이름을 입력해 주세요 :)")

    if name == "고구마":
        st.success(f"{name}님 반갑습니다!")
    elif name:
        st.error("고구마님이 아니네요...")

    gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
    st.write("선택한 성별:", gender)

# -----------------------------
# 📷 카메라 입력 탭
# -----------------------------
with tab7:
    image_data = st.camera_input("사진을 찍어보세요")
    if image_data:
        st.image(image_data)

# -----------------------------
# 🤖 GPT 탭
# -----------------------------
with tab8:
    user_api_key = st.secrets["openai"]["api_key"]

    if user_api_key:
        from openai import OpenAI

        client = OpenAI(api_key=user_api_key)
        prompt = st.text_input("프롬프트를 입력해주세요.")

        if prompt:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
  


# import streamlit as st

# # -----------------------------
# # 🎈 제목 및 소개 섹션
# # -----------------------------
# st.title("🎈 손정우의 첫 번째 앱")
# st.info("안녕하세요 반갑습니다. 저는 손정우 입니다.")
# st.write("안녕하세요 반갑습니다. 저는 손정우 입니다")

# # -----------------------------
# # 🧱 페이지 구조 섹션
# # -----------------------------
# st.title("위")
# st.header("중간")
# st.subheader("아래")

# # -----------------------------
# # 🖼️ 이미지 섹션
# # -----------------------------
# st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
# st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWI2Y2l4dmdqOWxnZWplazN5dHQ2bXJubTU4NWEzMmFkaXZjMWJldiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HeiJ27Z2DDrzvrlcW0/giphy.gif")

# # -----------------------------
# # 🔗 외부 링크 버튼
# # -----------------------------
# st.title("Hello")
# st.link_button("tetr.io", "https://tetr.io/")

# # -----------------------------
# # 📊 열(Column) 레이아웃 섹션
# # -----------------------------
# col1, col2 = st.columns(2)

# with col1:
#     st.write("왼쪽 열입니다.")
# with col2:
#     st.write("오른쪽 열입니다.")

# # -----------------------------
# # 📁 탭(Tab) UI
# # -----------------------------
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])

# with tab1:
#     st.write("탭 1111111111111111.")
# with tab2:
#     st.write("탭 2222222222222222.")

# # -----------------------------
# # 👤 사용자 입력 처리
# # -----------------------------
# name = st.text_input("이름을 입력해 주세요 :)")

# if name == "고구마":
#     st.success(f"{name}님 반갑습니다!")
# elif name:
#     st.error("고구마님이 아니네요...")

# # -----------------------------
# # ⚧ 성별 선택
# # -----------------------------
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.write("선택한 성별:", gender)

# # -----------------------------
# # 📷 카메라 입력
# # -----------------------------
# image_data = st.camera_input("사진을 찍어보세요")
# if image_data:
#     st.image(image_data)

# # -----------------------------
# # 📌 사이드바 메뉴
# # -----------------------------
# st.sidebar.title("📌 사이드바 메뉴")
# option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
# st.write("선택한 옵션:", option)

# # -----------------------------
# # 🤖 OpenAI API 연동 (GPT)
# # -----------------------------
# import openai

# user_api_key=st.secrets["openai"]["api_key"]

# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key=user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     if prompt:
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         st.markdown("### 💡 GPT의 답변:")
#         st.write(completion.choices[0].message.content)

# import streamlit as st

# st.title("🎈 손정우의 첫 번쨰 앱")
# st.info(
#     "안녕하세요 반갑습니다. 저는 손정우 입니다."
# )
# st.write(
#     " 안녕하세요 반갑습니다. 저는 손정우 입니다"
# )
# # 페이지 구조용 제목 출력
# st.title("위")
# st.header("중간")
# st.subheader("아래")
# st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
# st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWI2Y2l4dmdqOWxnZWplazN5dHQ2bXJubTU4NWEzMmFkaXZjMWJldiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HeiJ27Z2DDrzvrlcW0/giphy.gif")
# import streamlit as st
# st.title("Hello")
# st.link_button("tetr.io","https://tetr.io/")
# # st.columns(n): 화면을 n개의 수직 열로 나눕니다
# col1, col2 = st.columns(2)  # 2개의 열 생성

# with col1:
#     st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
# with col2:
#     st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
#     # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

# with tab1:
#     st.write("탭 1111111111111111.")  # 첫 번째 탭에 표시할 내용
# with tab2:
#     st.write("탭 2222222222222222.")  # 두 번째 탭에 표시할 내용

# name=st.text_input("이름을 임력해 주세요:)")

# if name=="고구마":
#     st.success(name+"님 반갑습니다!")
# else:
#     st.error("고구마님이 아니네요...")

# # 여러 옵션 중 하나 선택
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.write("선택한 성별:", gender)
# # 카메라로 사진 촬영
# image_data = st.camera_input("사진을 찍어보세요")
# if image_data:
#     st.image(image_data)
# # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
# st.sidebar.title("📌 사이드바 메뉴")
# option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
# st.write("선택한 옵션:", option)


# import openai

# user_api_key = st.text_input("키를 입력해주세요.")

# if user_api_key:

#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

