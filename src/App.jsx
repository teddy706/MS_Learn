import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import ProgressOverview from './components/ProgressOverview';
import ModuleList from './components/ModuleList';
import Flashcards from './components/Flashcards';
import StudyTimer from './components/StudyTimer';
import QuickNotesModal from './components/QuickNotesModal';

import { modulesData as ab100Modules } from './data/modulesData';
import { flashcardsData as ab100Cards } from './data/flashcardsData';
import { ai103ModulesData } from './data/ai103ModulesData';
import { ai103FlashcardsData } from './data/ai103FlashcardsData';

import { BookOpen, Sparkles, Timer } from 'lucide-react';

export default function App() {
  // Current Active Exam Track: 'ab100' | 'ai103'
  const [currentExam, setCurrentExam] = useState(() => {
    return localStorage.getItem('selected_exam_track') || 'ab100';
  });

  // Theme state
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem('ab100_theme') || 'light';
  });

  // Active tab state: 'roadmap' | 'flashcards' | 'timer'
  const [activeTab, setActiveTab] = useState('roadmap');

  // Select active modules & flashcards based on currentExam
  const activeModulesData = currentExam === 'ab100' ? ab100Modules : ai103ModulesData;
  const activeFlashcardsData = currentExam === 'ab100' ? ab100Cards : ai103FlashcardsData;

  // Completed unit IDs stored per exam track
  const storageKeyUnits = `completed_units_${currentExam}`;
  const storageKeyNotes = `user_notes_${currentExam}`;

  const [completedUnitIds, setCompletedUnitIds] = useState([]);
  const [userNotes, setUserNotes] = useState({});

  // Load state whenever currentExam changes
  useEffect(() => {
    localStorage.setItem('selected_exam_track', currentExam);
    
    try {
      const savedUnits = localStorage.getItem(storageKeyUnits);
      setCompletedUnitIds(savedUnits ? JSON.parse(savedUnits) : []);
    } catch (e) {
      setCompletedUnitIds([]);
    }

    try {
      const savedNotes = localStorage.getItem(storageKeyNotes);
      setUserNotes(savedNotes ? JSON.parse(savedNotes) : {});
    } catch (e) {
      setUserNotes({});
    }
  }, [currentExam]);

  // Active note modal state
  const [activeNoteUnit, setActiveNoteUnit] = useState(null);

  // Sync theme
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('ab100_theme', theme);
  }, [theme]);

  // Sync completed units to localStorage
  useEffect(() => {
    if (currentExam) {
      localStorage.setItem(storageKeyUnits, JSON.stringify(completedUnitIds));
    }
  }, [completedUnitIds, currentExam]);

  // Sync notes to localStorage
  useEffect(() => {
    if (currentExam) {
      localStorage.setItem(storageKeyNotes, JSON.stringify(userNotes));
    }
  }, [userNotes, currentExam]);

  const toggleTheme = () => {
    setTheme(prev => (prev === 'dark' ? 'light' : 'dark'));
  };

  const handleToggleUnit = (unitId) => {
    setCompletedUnitIds(prev => 
      prev.includes(unitId) ? prev.filter(id => id !== unitId) : [...prev, unitId]
    );
  };

  const handleSaveNote = (unitId, text) => {
    setUserNotes(prev => ({
      ...prev,
      [unitId]: text
    }));
  };

  const handleResetProgress = () => {
    const examLabel = currentExam === 'ab100' ? 'AB-100' : 'AI-103';
    if (window.confirm(`[${examLabel}] 트랙의 모든 학습 진도 및 체크 상태를 초기화하시겠습니까?`)) {
      setCompletedUnitIds([]);
    }
  };

  // Count total units across active modules
  const totalUnits = activeModulesData.reduce((acc, curr) => acc + curr.units.length, 0);

  return (
    <div className="app-container">
      <Header 
        currentExam={currentExam}
        setCurrentExam={setCurrentExam}
        theme={theme} 
        toggleTheme={toggleTheme} 
        onResetProgress={handleResetProgress} 
      />

      <main className="main-content">
        {/* Progress Card Overview */}
        <ProgressOverview 
          totalUnits={totalUnits}
          completedUnitIds={completedUnitIds}
          modulesData={activeModulesData}
        />

        {/* Tab Navigation */}
        <div className="tabs-nav">
          <button
            className={`tab-btn ${activeTab === 'roadmap' ? 'active' : ''}`}
            onClick={() => setActiveTab('roadmap')}
          >
            <BookOpen size={18} />
            <span>학습 로드맵 ({activeModulesData.length}개 모듈, {totalUnits}개 단원)</span>
          </button>

          <button
            className={`tab-btn ${activeTab === 'flashcards' ? 'active' : ''}`}
            onClick={() => setActiveTab('flashcards')}
          >
            <Sparkles size={18} />
            <span>핵심 암기 플래시 카드 ({activeFlashcardsData.length}개)</span>
          </button>

          <button
            className={`tab-btn ${activeTab === 'timer' ? 'active' : ''}`}
            onClick={() => setActiveTab('timer')}
          >
            <Timer size={18} />
            <span>뽀모도로 타이머</span>
          </button>
        </div>

        {/* Tab Contents */}
        {activeTab === 'roadmap' && (
          <ModuleList 
            modulesData={activeModulesData}
            completedUnitIds={completedUnitIds}
            onToggleUnit={handleToggleUnit}
            onOpenNotes={(unit) => setActiveNoteUnit(unit)}
            userNotes={userNotes}
          />
        )}

        {activeTab === 'flashcards' && (
          <Flashcards flashcardsData={activeFlashcardsData} />
        )}

        {activeTab === 'timer' && (
          <StudyTimer />
        )}
      </main>

      {/* Note Modal */}
      {activeNoteUnit && (
        <QuickNotesModal
          unit={activeNoteUnit}
          currentNote={userNotes[activeNoteUnit.id] || ''}
          onSave={handleSaveNote}
          onClose={() => setActiveNoteUnit(null)}
        />
      )}

      {/* Footer */}
      <footer className="footer">
        Microsoft Exam Study Hub &copy; {new Date().getFullYear()} AB-100 &amp; AI-103 Learning Guide. Powered by Microsoft Learn Official Content.
      </footer>
    </div>
  );
}
