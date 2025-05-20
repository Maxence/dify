import React, { useCallback } from 'react'
import { useTranslation } from 'react-i18next'
import produce from 'immer'
import { RiFile2Fill } from '@remixicon/react'
import FeatureCard from '@/app/components/base/features/new-feature-panel/feature-card'
import { useFeatures, useFeaturesStore } from '@/app/components/base/features/hooks'
import type { OnFeaturesChange } from '@/app/components/base/features/types'
import { FeatureEnum } from '@/app/components/base/features/types'

type Props = {
  disabled?: boolean
  onChange?: OnFeaturesChange
}

const FileOnlyMessage = ({
  disabled,
  onChange,
}: Props) => {
  const { t } = useTranslation()
  const features = useFeatures(s => s.features)
  const featuresStore = useFeaturesStore()

  const handleChange = useCallback((type: FeatureEnum, enabled: boolean) => {
    const {
      features,
      setFeatures,
    } = featuresStore!.getState()

    const newFeatures = produce(features, (draft) => {
      draft[type] = {
        ...draft[type],
        enabled,
      }
    })
    setFeatures(newFeatures)
    if (onChange)
      onChange(newFeatures)
  }, [featuresStore, onChange])

  return (
    <FeatureCard
      icon={
        <div className='shrink-0 rounded-lg border-[0.5px] border-divider-subtle bg-util-colors-blue-blue-600 p-1 shadow-xs'>
          <RiFile2Fill className='h-4 w-4 text-text-primary-on-surface' />
        </div>
      }
      title={t('appDebug.feature.fileOnlyMessage.title')}
      value={!!features.fileOnlyMessage?.enabled}
      description={t('appDebug.feature.fileOnlyMessage.description')!}
      onChange={state => handleChange(FeatureEnum.fileOnlyMessage, state)}
      disabled={disabled}
    />
  )
}

export default FileOnlyMessage
