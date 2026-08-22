import React, { useState } from 'react';
import ModuleCard from './ModuleCard';
import { Search, Filter, CheckCircle2 } from 'lucide-react';

export default function ModuleList({ 
  modulesData, 
  completedUnitIds, 
  onToggleUnit, 
  onOpenNotes,
  userNotes 
}) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [hideCompleted, setHideCompleted] = useState(false);

  // Extract unique categories
  const categories = ['All', ...new Set(modulesData.map(m => m.category))];

  // Filter modules and units
  const filteredModules = modulesData.map(module => {
    // Check if module matches category
    const categoryMatches = selectedCategory === 'All' || module.category === selectedCategory;
    if (!categoryMatches) return null;

    // Filter units by search query
    const matchingUnits = module.units.filter(unit => {
      const titleMatch = unit.title.toLowerCase().includes(searchQuery.toLowerCase());
      const moduleMatch = module.title.toLowerCase().includes(searchQuery.toLowerCase());
      const isCompleted = completedUnitIds.includes(unit.id);
      
      if (hideCompleted && isCompleted) return false;
      return titleMatch || moduleMatch;
    });

    if (matchingUnits.length === 0 && searchQuery.trim() !== '') {
      return null;
    }

    return {
      ...module,
      units: searchQuery.trim() !== '' ? matchingUnits : (hideCompleted ? module.units.filter(u => !completedUnitIds.includes(u.id)) : module.units)
    };
  }).filter(Boolean);

  return (
    <div>
      {/* Search and Filters controls */}
      <div className="controls-bar">
        <div className="search-wrapper">
          <Search className="search-icon" size={18} />
          <input
            type="text"
            className="search-input"
            placeholder="단원 제목 또는 키워드 검색 (예: Copilot Studio, ALM, ROI...)"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>

        <select
          className="category-select"
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
        >
          {categories.map(cat => (
            <option key={cat} value={cat}>
              {cat === 'All' ? '📌 모든 영역 (Category)' : cat}
            </option>
          ))}
        </select>

        <button
          className={`btn ${hideCompleted ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setHideCompleted(!hideCompleted)}
        >
          <CheckCircle2 size={16} />
          <span>{hideCompleted ? '완료된 단원 숨김중' : '완료 단원 포함'}</span>
        </button>
      </div>

      {/* Module List Output */}
      {filteredModules.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '3rem', color: 'var(--text-muted)' }}>
          🔍 검색 조건에 일치하는 모듈 또는 단원이 없습니다.
        </div>
      ) : (
        filteredModules.map((module, idx) => (
          <ModuleCard
            key={module.id}
            module={module}
            completedUnitIds={completedUnitIds}
            onToggleUnit={onToggleUnit}
            onOpenNotes={onOpenNotes}
            userNotes={userNotes}
            defaultExpanded={searchQuery.trim() !== '' || idx === 0}
          />
        ))
      )}
    </div>
  );
}
