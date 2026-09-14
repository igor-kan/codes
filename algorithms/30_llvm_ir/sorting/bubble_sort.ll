; ModuleID = 'algorithms/02_c/sorting/bubble_sort.c'
source_filename = "algorithms/02_c/sorting/bubble_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @bubble_sort(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = add i32 %1, -1
  %4 = icmp sgt i32 %1, 1
  br i1 %4, label %5, label %17

5:                                                ; preds = %2, %30
  %6 = phi i32 [ %32, %30 ], [ %3, %2 ]
  %7 = phi i32 [ %31, %30 ], [ 0, %2 ]
  %8 = zext i32 %6 to i64
  %9 = sub nsw i32 %7, %1
  %10 = icmp slt i32 %9, -1
  br i1 %10, label %11, label %30

11:                                               ; preds = %5
  %12 = load i32, ptr %0, align 4, !tbaa !5
  %13 = and i64 %8, 1
  %14 = icmp eq i32 %6, 1
  br i1 %14, label %20, label %15

15:                                               ; preds = %11
  %16 = and i64 %8, 4294967294
  br label %34

17:                                               ; preds = %30, %2
  ret void

18:                                               ; preds = %52
  %19 = icmp eq i64 %13, 0
  br i1 %19, label %30, label %20

20:                                               ; preds = %18, %11
  %21 = phi i32 [ %12, %11 ], [ %53, %18 ]
  %22 = phi i64 [ 0, %11 ], [ %46, %18 ]
  %23 = icmp ne i64 %13, 0
  tail call void @llvm.assume(i1 %23)
  %24 = getelementptr inbounds nuw i32, ptr %0, i64 %22
  %25 = getelementptr inbounds nuw i8, ptr %24, i64 4
  %26 = load i32, ptr %25, align 4, !tbaa !5
  %27 = icmp sgt i32 %21, %26
  br i1 %27, label %28, label %30

28:                                               ; preds = %20
  %29 = getelementptr inbounds nuw i32, ptr %0, i64 %22
  store i32 %26, ptr %29, align 4, !tbaa !5
  store i32 %21, ptr %25, align 4, !tbaa !5
  br label %30

30:                                               ; preds = %18, %28, %20, %5
  %31 = add nuw nsw i32 %7, 1
  %32 = add i32 %6, -1
  %33 = icmp eq i32 %31, %3
  br i1 %33, label %17, label %5, !llvm.loop !9

34:                                               ; preds = %52, %15
  %35 = phi i32 [ %12, %15 ], [ %53, %52 ]
  %36 = phi i64 [ 0, %15 ], [ %46, %52 ]
  %37 = phi i64 [ 0, %15 ], [ %54, %52 ]
  %38 = or disjoint i64 %36, 1
  %39 = getelementptr inbounds nuw i32, ptr %0, i64 %38
  %40 = load i32, ptr %39, align 4, !tbaa !5
  %41 = icmp sgt i32 %35, %40
  br i1 %41, label %42, label %44

42:                                               ; preds = %34
  %43 = getelementptr inbounds nuw i32, ptr %0, i64 %36
  store i32 %40, ptr %43, align 4, !tbaa !5
  store i32 %35, ptr %39, align 4, !tbaa !5
  br label %44

44:                                               ; preds = %34, %42
  %45 = phi i32 [ %40, %34 ], [ %35, %42 ]
  %46 = add nuw nsw i64 %36, 2
  %47 = getelementptr inbounds nuw i32, ptr %0, i64 %46
  %48 = load i32, ptr %47, align 4, !tbaa !5
  %49 = icmp sgt i32 %45, %48
  br i1 %49, label %50, label %52

50:                                               ; preds = %44
  %51 = getelementptr inbounds nuw i32, ptr %0, i64 %38
  store i32 %48, ptr %51, align 4, !tbaa !5
  store i32 %45, ptr %47, align 4, !tbaa !5
  br label %52

52:                                               ; preds = %50, %44
  %53 = phi i32 [ %48, %44 ], [ %45, %50 ]
  %54 = add i64 %37, 2
  %55 = icmp eq i64 %54, %16
  br i1 %55, label %18, label %34, !llvm.loop !11
}

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #1

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
