import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# 페이지 설정
st.set_page_config(
    page_title="포털 사이트",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS
st.markdown("""
<style>
    /* 메인 색상 */
    :root {
        --primary-color: #00C73C;
        --text-color: #000;
        --light-gray: #f5f5f5;
        --border-color: #e0e0e0;
    }
    
    /* 전체 배경 */
    .main {
        background-color: white;
    }
    
    /* 배너 스타일 */
    .banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 8px;
        color: white;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .banner h2 {
        margin: 0;
        font-size: 28px;
    }
    
    /* 탭 네비게이션 */
    .nav-tabs {
        display: flex;
        gap: 20px;
        padding: 15px 0;
        border-bottom: 2px solid #e0e0e0;
        margin-bottom: 30px;
    }
    
    .nav-tab {
        padding: 8px 15px;
        cursor: pointer;
        font-weight: 500;
        border-bottom: 3px solid transparent;
        transition: all 0.3s;
    }
    
    .nav-tab:hover {
        color: var(--primary-color);
    }
    
    .nav-tab.active {
        color: var(--primary-color);
        border-bottom-color: var(--primary-color);
    }
    
    /* 카드 스타일 */
    .news-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        overflow: hidden;
        transition: box-shadow 0.3s;
        cursor: pointer;
    }
    
    .news-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .news-card-img {
        width: 100%;
        height: 180px;
        background: #f0f0f0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
    }
    
    .news-card-body {
        padding: 15px;
    }
    
    .news-card-title {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
        line-height: 1.4;
        color: #333;
    }
    
    .news-card-meta {
        font-size: 12px;
        color: #999;
    }
    
    .news-card-source {
        display: inline-block;
        background: #ff6b6b;
        color: white;
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 11px;
        margin-right: 8px;
    }
    
    /* 섹션 제목 */
    .section-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid var(--primary-color);
    }
    
    /* 상품 리스트 */
    .product-item {
        padding: 12px;
        border-bottom: 1px solid #e0e0e0;
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .product-item:hover {
        background-color: #f5f5f5;
    }
    
    .product-name {
        font-weight: 600;
        font-size: 13px;
        margin-bottom: 4px;
    }
    
    .product-price {
        color: var(--primary-color);
        font-weight: bold;
    }
    
    /* 사이드바 */
    .sidebar-category {
        padding: 10px 0;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .sidebar-category-title {
        font-weight: 600;
        cursor: pointer;
        padding: 10px 0;
    }
    
    .sidebar-item {
        padding: 6px 0;
        padding-left: 20px;
        font-size: 13px;
        cursor: pointer;
        color: #666;
    }
    
    .sidebar-item:hover {
        color: var(--primary-color);
    }
</style>
""", unsafe_allow_html=True)

# 더미 데이터 생성
def generate_news_data(count=8):
    news_sources = ["뉴스통", "기자뉴스", "스포츠뉴스", "연예뉴스"]
    news_titles = [
        "新규제 강화로 시장 변동성 확대",
        "기술 업체 신제품 발표회 개최",
        "스포츠 스타 특별 인터뷰",
        "연예인 소식",
        "경제 뉴스 속보",
        "날씨 예보 안내",
        "부동산 시장 분석",
        "증권 투자 정보"
    ]
    emojis = ["📰", "💼", "⚽", "🎬", "📊", "🌤️", "🏠", "💹"]
    
    data = []
    for i in range(count):
        data.append({
            "source": random.choice(news_sources),
            "title": news_titles[i % len(news_titles)],
            "emoji": emojis[i % len(emojis)],
            "time": f"{random.randint(1, 12)}월 {random.randint(10, 28)}일 {random.randint(8, 18):02d}:{random.randint(0, 59):02d}",
        })
    return data

def generate_products(count=10):
    categories = ["패션", "뷰티", "식품", "전자기기", "가구", "스포츠"]
    brands = ["미니 내디", "CJ스타일", "GS샵", "쿠팡", "올리브영", "SSG닷컴"]
    
    data = []
    for i in range(count):
        data.append({
            "category": random.choice(categories),
            "brand": random.choice(brands),
            "name": f"인기 상품 #{i+1}",
            "price": f"{random.randint(10, 500) * 1000:,}원"
        })
    return data

# 세션 상태 초기화
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "뉴스"

if "news_data" not in st.session_state:
    st.session_state.news_data = generate_news_data()

if "products_data" not in st.session_state:
    st.session_state.products_data = generate_products()

# 상단 배너
st.markdown("""
<div class="banner">
    <h2>🌟 포털 사이트</h2>
    <p>정보의 중심, 여기서 모든 것을 찾으세요</p>
</div>
""", unsafe_allow_html=True)

# 검색 바
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    search_query = st.text_input(
        "검색",
        placeholder="검색어를 입력하세요",
        label_visibility="collapsed"
    )

# 네비게이션 탭
tabs = ["뉴스", "스포츠", "엔터", "쇼핑", "증권", "부동산"]
st.markdown("<div class='nav-tabs'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("📰 뉴스", use_container_width=True):
        st.session_state.active_tab = "뉴스"

with col2:
    if st.button("⚽ 스포츠", use_container_width=True):
        st.session_state.active_tab = "스포츠"

with col3:
    if st.button("🎬 엔터", use_container_width=True):
        st.session_state.active_tab = "엔터"

with col4:
    if st.button("🛍️ 쇼핑", use_container_width=True):
        st.session_state.active_tab = "쇼핑"

with col5:
    if st.button("💹 증권", use_container_width=True):
        st.session_state.active_tab = "증권"

with col6:
    if st.button("🏠 부동산", use_container_width=True):
        st.session_state.active_tab = "부동산"

st.markdown("</div>", unsafe_allow_html=True)

# 메인 콘텐츠 영역
st.markdown("---")

# 레이아웃: 메인 콘텐츠 + 사이드바
main_col, sidebar_col = st.columns([3, 1])

# 메인 콘텐츠
with main_col:
    if st.session_state.active_tab == "뉴스":
        st.markdown("<div class='section-title'>📰 실시간 뉴스</div>", unsafe_allow_html=True)
        
        # 뉴스 그리드 (2x4)
        news = st.session_state.news_data
        
        for row in range(0, len(news), 4):
            cols = st.columns(4)
            for idx, col in enumerate(cols):
                if row + idx < len(news):
                    item = news[row + idx]
                    with col:
                        st.markdown(f"""
                        <div class='news-card'>
                            <div class='news-card-img'>{item['emoji']}</div>
                            <div class='news-card-body'>
                                <div class='news-card-source'>{item['source']}</div>
                                <div class='news-card-title'>{item['title']}</div>
                                <div class='news-card-meta'>{item['time']}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    elif st.session_state.active_tab == "쇼핑":
        st.markdown("<div class='section-title'>🛍️ 인기 상품</div>", unsafe_allow_html=True)
        
        products = st.session_state.products_data
        for row in range(0, len(products), 3):
            cols = st.columns(3)
            for idx, col in enumerate(cols):
                if row + idx < len(products):
                    item = products[row + idx]
                    with col:
                        st.markdown(f"""
                        <div class='news-card'>
                            <div class='news-card-img'>🛒</div>
                            <div class='news-card-body'>
                                <div class='news-card-source'>{item['brand']}</div>
                                <div class='news-card-title'>{item['name']}</div>
                                <div class='product-price'>{item['price']}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    
    else:
        st.markdown(f"<div class='section-title'>{st.session_state.active_tab}</div>", unsafe_allow_html=True)
        st.info(f"'{st.session_state.active_tab}' 섹션의 콘텐츠를 구현하세요.")

# 사이드바 콘텐츠
with sidebar_col:
    st.markdown("<div class='section-title' style='font-size: 16px;'>🔍 카테고리</div>", unsafe_allow_html=True)
    
    categories = {
        "쇼핑": ["패션", "뷰티", "식품", "전자기기"],
        "뉴스": ["정치", "경제", "사회", "과학"],
        "생활": ["날씨", "지도", "부동산", "자동차"]
    }
    
    for category_group, items in categories.items():
        st.markdown(f"**{category_group}**")
        for item in items:
            if st.button(item, use_container_width=True, key=f"cat_{item}"):
                st.success(f"{item} 선택됨!")
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# 푸터
st.markdown("""
<div style='text-align: center; color: #999; font-size: 12px; margin-top: 30px;'>
    <p>© 2025 포털 사이트 | 회사소개 | 이용약관 | 개인정보처리방침</p>
</div>
""", unsafe_allow_html=True)
