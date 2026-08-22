import React from 'react';
import { BookOpen, Moon, Sun, RefreshCw, Cpu, Layers } from 'lucide-react';

export default function Header({ currentExam, setCurrentExam, theme, toggleTheme, onResetProgress }) {
  return (
    <header className="header-wrapper">
      <div className="header-inner">
        <div className="brand-section">
          {/* Exam Selector Switcher */}
          <div className="exam-selector-group">
            <button
              className={`exam-chip ${currentExam === 'ab100' ? 'active' : ''}`}
              onClick={() => setCurrentExam('ab100')}
              title="AB-100: Architect Agentic AI Business Solutions"
            >
              <Layers size={15} />
              <span>AB-100</span>
            </button>

            <button
              className={`exam-chip ${currentExam === 'ai103' ? 'active' : ''}`}
              onClick={() => setCurrentExam('ai103')}
              title="AI-103: Developing Generative AI & Agents on Azure"
            >
              <Cpu size={15} />
              <span>AI-103</span>
            </button>
          </div>

          <h1 className="brand-title">
            <BookOpen className="w-5 h-5 text-primary" style={{ color: 'var(--primary)' }} />
            <span>
              {currentExam === 'ab100' 
                ? 'Architect Agentic AI Business Solutions' 
                : 'Azure 생성 AI 앱 및 에이전트 개발 (AI-103)'}
            </span>
          </h1>
        </div>

        <div className="header-actions">
          <button 
            className="btn btn-secondary" 
            onClick={onResetProgress}
            title="현재 시험 학습 진도율 초기화"
          >
            <RefreshCw size={15} />
            <span>진도 초기화</span>
          </button>

          <button 
            className="btn-icon" 
            onClick={toggleTheme} 
            title={theme === 'dark' ? "라이트 모드로 변경" : "다크 모드로 변경"}
          >
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </div>
      </div>
    </header>
  );
}
