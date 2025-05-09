import streamlit as st

st.title("🎈 손정우의 첫 번쨰 앱")
st.info(
    "안녕하세요 반갑습니다. 저는 손정우 입니다."
)
st.write(
    " 안녕하세요 반갑습니다. 저는 손정우 입니다"
)
# 페이지 구조용 제목 출력
st.title("위")
st.header("중간")
st.subheader("아래")
st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWI2Y2l4dmdqOWxnZWplazN5dHQ2bXJubTU4NWEzMmFkaXZjMWJldiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HeiJ27Z2DDrzvrlcW0/giphy.gif")
import streamlit as st
st.title("Hello")
st.link_button("tetr.io","https://tetr.io/")
# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1111111111111111.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2222222222222222.")  # 두 번째 탭에 표시할 내용
st.balloons()
name=st.text_input("이름을 임력해 주세요:)")

if name=="고구마":
    st.success(name+"님 반갑습니다!")
else:
    st.error("고구마님이 아니네요...")

st.error(name+"님 반갑습니다!")
# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)
# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)